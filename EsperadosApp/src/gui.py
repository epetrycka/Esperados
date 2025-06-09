import sys
import os
import tempfile
import io
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QMessageBox, QPlainTextEdit, QLabel, QHBoxLayout,
    QFrame, QTextEdit   
)
from antlr4 import *
from generated.EsperadosLexer import EsperadosLexer
from generated.EsperadosParser import EsperadosParser
from visitor import EsperadosVisitorImpl
from error_handler import ErrorListener
from PyQt5.QtWidgets import QInputDialog

from PyQt5.QtGui import (
    QSyntaxHighlighter, QTextCharFormat, QColor, QFont, QPainter
)
from PyQt5.QtCore import Qt, QRegExp, QRect, QSize
from PyQt5.QtWidgets import QFileDialog

sys.setrecursionlimit(100000)

class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)

class CodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = LineNumberArea(self)
        self.setFont(QFont("Consolas", 12))
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                selection-background-color: #264f78;
                border: 1px solid #3c3c3c;
            }
        """)
        
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.updateLineNumberAreaWidth(0)

    def lineNumberAreaWidth(self):
        digits = 1
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num /= 10
            digits += 1
        space = 10 + self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), QColor("#252526"))
        
        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(QColor("#858585"))
                painter.drawText(0, int(top), self.lineNumberArea.width() - 5, self.fontMetrics().height(),
                                Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

class EsperadosHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#e9c46a"))
        keywords = ['vere', 'malvero', 'haltu', 'daurigi', 'reveni']

        self.highlighting_rules = [(QRegExp(r'\b' + kw + r'\b'), keyword_format) for kw in keywords]

        keyword_format2 = QTextCharFormat()
        keyword_format2.setForeground(QColor("#e76f51"))
        keywords2 = ['Saluton', 'Adiau']

        for kw in keywords2:
            pattern = QRegExp(r'\b' + kw + r'\b')
            self.highlighting_rules.append((pattern, keyword_format2))

        keyword_format3 = QTextCharFormat()
        keyword_format3.setForeground(QColor("#5cb4bf"))
        keywords3 = ['variablo', 'por ciu', 'en', 'alie se', 'se', 'alie', 'por', 'gis', 'difini', 'forigi', 'funcio']

        for kw in keywords3:
            pattern = QRegExp(r'\b' + kw + r'\b')
            self.highlighting_rules.append((pattern, keyword_format3))

        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#2a9d8f"))
        self.highlighting_rules.append((QRegExp(r'\b[0-9]+(\.[0-9]+)?\b'), number_format))

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#f4e5be"))
        self.highlighting_rules.append((QRegExp(r'"[^"]*"'), string_format))
        self.highlighting_rules.append((QRegExp(r"'[^']*'"), string_format))

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#264653"))
        comment_format.setFontItalic(True)
        self.highlighting_rules.append((QRegExp(r':O[^\n]*'), comment_format))
        self.highlighting_rules.append((QRegExp(r':P[^\n]*P:'), comment_format))

    def highlightBlock(self, text):
        for pattern, fmt in self.highlighting_rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)
        self.setCurrentBlockState(0)

class EsperadosIDE(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Esperados")
        self.resize(1200, 800)
        self.setStyleSheet("""
            QWidget {
                background-color: #252526;
                color: #d4d4d4;
            }
            QPushButton {
                background-color: #0e639c;
                color: white;
                border: none;
                padding: 5px 15px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #1177bb;
            }
            QLabel {
                color: #d4d4d4;
            }
        """)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Top panel - title and buttons
        top_panel = QHBoxLayout()
        title_label = QLabel("Esperados")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        top_panel.addWidget(title_label)
        top_panel.addStretch()
        
        self.run_button = QPushButton("Run (Ctrl+Enter)")
        self.run_button.setShortcut("Ctrl+Return")
        self.run_button.clicked.connect(self.run_parser)
        self.run_button.setStyleSheet("background-color: #f4a261")
        top_panel.addWidget(self.run_button)
        
        main_layout.addLayout(top_panel)

        # Main area - editor and output
        editor_output_layout = QHBoxLayout()
        editor_output_layout.setSpacing(10)

        # Code editor with line numbers
        self.editor = CodeEditor()
        self.editor.setPlaceholderText("Enter Esperados code here...")
        self.highlighter = EsperadosHighlighter(self.editor.document())
        editor_output_layout.addWidget(self.editor, 3)

        # Output area
        output_frame = QFrame()
        output_frame.setFrameShape(QFrame.StyledPanel)
        output_frame.setStyleSheet("background-color: #1e1e1e; border: 1px solid #3c3c3c;")
        output_layout = QVBoxLayout(output_frame)
        output_layout.setContentsMargins(5, 5, 5, 5)
        
        output_label = QLabel("Output:")
        output_label.setStyleSheet("font-weight: bold;")
        output_layout.addWidget(output_label)
        
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setFont(QFont("Consolas", 11))
        self.output_area.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: none;
            }
        """)

        output_layout.addWidget(self.output_area)
        
        editor_output_layout.addWidget(output_frame, 1)
        
        # buttons
        self.import_button = QPushButton("Open file")
        self.import_button.clicked.connect(self.import_code)
        self.import_button.setStyleSheet("background-color : #2a9d8f")
        top_panel.addWidget(self.import_button)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_code)
        self.save_button.setStyleSheet("background-color : #2a9d8f")
        top_panel.addWidget(self.save_button)


        main_layout.addLayout(editor_output_layout)

        # Status bar
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: #858585; font-size: 11px;")
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

    def run_parser(self):
        code = self.editor.toPlainText().strip()
        self.output_area.clear()
        self.status_label.setText("Processing...")

        visitor = EsperadosVisitorImpl(input_provider=self.get_input_from_user)
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".es", mode='w', encoding='utf-8') as tmp_file:
                tmp_file.write(code)
                tmp_path = tmp_file.name

            input_stream = FileStream(tmp_path, encoding='utf-8')
            lexer = EsperadosLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = EsperadosParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(ErrorListener())

            try:
                tree = parser.program()
            except Exception as syntax_error:
                self.output_area.setHtml(f'<span style="color: red;">{str(syntax_error)}</span>')
                # self.output_area.setPlainText(str(syntax_error))
                self.status_label.setText("Finished with syntax error")
                return

            if parser.getNumberOfSyntaxErrors() > 0:
                self.output_area.setPlainText("Syntax errors detected.")
                self.status_label.setText("Finished with errors")
                return

            buffer = io.StringIO()
            sys_stdout_original = sys.stdout
            sys.stdout = buffer

            try:
                visitor = EsperadosVisitorImpl(input_provider=self.get_input_from_user)
                visitor.visit(tree)

            finally:
                sys.stdout = sys_stdout_original

            result = buffer.getvalue().strip()
            if not result:
                result = "Code executed successfully, no output."

            self.output_area.setPlainText(result)
            self.status_label.setText("Finished successfully")

        except Exception as e:
            self.output_area.setHtml(f'<span style="color: red;">{str(e).replace("\033[91m", "").replace("\033[0m", "").replace("\t", "").replace("\n", "<br>")}</span>')
            self.status_label.setText("Finished with errors")


    def import_code(self):
        path, _ = QFileDialog.getOpenFileName(self, "Import code", "", "Esperados files (*.es);;All files (*)")
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.editor.setPlainText(content)
                self.status_label.setText(f"Loaded: {os.path.basename(path)}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not load the file:\n{e}")

    def save_code(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save code", "", "Esperados files (*.es);;All files (*)")
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(self.editor.toPlainText())
                self.status_label.setText(f"Saved: {os.path.basename(path)}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save the file:\n{e}")

    def get_input_from_user(self, prompt="Input: "):
        text, ok = QInputDialog.getText(self, "Esperados Input", prompt)
        if ok:
            return text
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EsperadosIDE()
    window.show()
    sys.exit(app.exec_())
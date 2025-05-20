from antlr4 import *
from src.generated.EsperadosLexer import EsperadosLexer
from src.generated.EsperadosParser import EsperadosParser
from src.visitor import EsperadosVisitorImpl
from src.error_handler import ErrorListener
import pytest

def run_code(code: str):
    input = InputStream(code)
    lexer = EsperadosLexer(input)
    stream = CommonTokenStream(lexer)
    parser = EsperadosParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ErrorListener())
    tree = parser.program()
    visitor = EsperadosVisitorImpl()
    result = visitor.visit(tree)
    return result

def test_empty_file(capsys):
    with open("tests/examples/incomplete_files/empty_file.es") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_correct_empty_file(capsys):
    with open(f"tests/examples/incomplete_files/correct_empty_file.es") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    assert captured.out == "👋 Saluton!\n👋 Adiau!\n"

@pytest.mark.parametrize("filename, expected", [
    ("incomplete_files/without_adiau.es", "program must end with Adiau"),
    ("incomplete_files/without_saluton.es", "program must begin with Saluton"),
    ("incomplete_files/adiau_before_saluton.es", "program must begin with Saluton"),
])

def test_saluton_adiau(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    with pytest.raises(Exception) as exc_info:
        run_code(code)
    assert expected in str(exc_info.value)

@pytest.mark.parametrize("filename, expected", [
    ("print_statement/example_1.es", "Prosty print"),
    ("print_statement/example_2.es", "Print z kilkoma danymi po przecinku"),
    ("print_statement/example_3.es", "Wypisywanie zmiennej 52.8 z pamieci"),
])

def test_print_statements(filename, expected, capsys):
    with open(f"tests/examples/{filename}") as f:
        code = f.read()
    _ = run_code(code)
    captured = capsys.readouterr()
    assert expected in captured.out


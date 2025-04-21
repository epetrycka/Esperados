import sys
from antlr4 import *
from generated.EsperandoLexer import EsperandoLexer
from generated.EsperandoParser import EsperandoParser
from visitor import EsperandoVisitorImpl

def main(argv):
    if len(argv) < 2:
        raise AttributeError("Not enough arguments. Please provide a file with code (with .es extension) as an argument.")
    try:
        input_stream = FileStream(argv[1], encoding='utf-8')
        lexer = EsperandoLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = EsperandoParser(stream)
        tree = parser.program()

        with open("tree.txt", "w") as file:
            file.write(tree.toStringTree(recog=parser).replace(") (", ")\n("))

        visitor = EsperandoVisitorImpl()
        visitor.visit(tree)
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main(sys.argv)
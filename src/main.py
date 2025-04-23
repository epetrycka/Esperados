import sys
from antlr4 import *
from generated.EsperadosLexer import EsperadosLexer
from generated.EsperadosParser import EsperadosParser
from visitor import EsperadosVisitorImpl

def main(argv):
    if len(argv) < 2:
        raise AttributeError("Not enough arguments. Please provide a file with code (with .es extension) as an argument.")
    try:
        input_stream = FileStream(argv[1], encoding='utf-8')
        lexer = EsperadosLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = EsperadosParser(stream)
        tree = parser.program()

        # with open(f"{argv[1]}_tree.txt", "w") as file:
        #     file.write(tree.toStringTree(recog=parser).replace(") (", ")\n("))

        visitor = EsperadosVisitorImpl()
        visitor.visit(tree)
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main(sys.argv)
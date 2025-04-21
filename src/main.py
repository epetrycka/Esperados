import sys
from antlr4 import *
from generated.EsperandoLexer import EsperandoLexer
from generated.EsperandoParser import EsperandoParser
from visitor import EsperandoVisitorImpl

def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = EsperandoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = EsperandoParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    visitor = EsperandoVisitorImpl()
    visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
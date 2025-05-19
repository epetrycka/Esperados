import sys
import os
from antlr4 import *
from generated.EsperadosLexer import EsperadosLexer
from generated.EsperadosParser import EsperadosParser
from visitor import EsperadosVisitorImpl
from visualize_tree import visualize_tree

def main(argv):
    if len(argv) < 2:
        raise AttributeError("Not enough arguments. Please provide a file with code (with .es extension) as an argument.")
    try:
        input_stream = FileStream(argv[1], encoding='utf-8')
        lexer = EsperadosLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = EsperadosParser(stream)
        tree = parser.program()
        visitor = EsperadosVisitorImpl()
        visitor.visit(tree)

        base_name = os.path.splitext(os.path.basename(argv[1]))[0]
        output_dir = os.path.join(os.path.dirname(argv[1]), "..", "Examples")
        output_file = os.path.join(output_dir, base_name + '_tree')

        with open(f"{output_file}.txt", "w") as file:
            file.write(tree.toStringTree(recog=parser).replace(") (", ")\n("))

        visualize_tree(tree, parser, base_name)

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main(sys.argv)
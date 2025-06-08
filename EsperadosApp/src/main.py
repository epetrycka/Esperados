import sys
import threading
import os
from antlr4 import *
from generated.EsperadosLexer import EsperadosLexer
from generated.EsperadosParser import EsperadosParser
from visitor import EsperadosVisitorImpl
from visualize_tree import visualize_tree
from error_handler import ErrorListener

def main(argv):
    sys.setrecursionlimit(100000)
    if len(argv) < 2:
        raise AttributeError("Not enough arguments. Please provide a file with code (with .es extension) as an argument.")
    try:
        input_stream = FileStream(argv[1], encoding='utf-8')
        lexer = EsperadosLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = EsperadosParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ErrorListener())
        tree = parser.program()
        if parser.getNumberOfSyntaxErrors() > 0:
            print("syntax errors")
        else:
            visitor = EsperadosVisitorImpl()
            visitor.visit(tree)

        base_name = os.path.splitext(os.path.basename(argv[1]))[0]
        output_dir = os.path.join(os.path.dirname(argv[1]), "trees")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, base_name + '_tree')

        with open(f"{output_file}.txt", "w") as file:
            file.write(tree.toStringTree(recog=parser).replace(") (", ")\n("))

        visualize_tree(tree, parser, base_name, argv[1])
        
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    threading.stack_size(32 * 1024 * 1024)

    t = threading.Thread(target=main, args=(sys.argv,))
    t.daemon = True
    t.start()
    t.join()
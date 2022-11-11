# Ping Pong Club Python file

# --- IMPORTS ---
import sys
from antlr4 import *
from lexer import Lexer
from parser import Parser

def main(argv):
    if len(sys.argv) > 1:
        in = FileStream(sys.argv[1])
    else:
        in = InputStream(sys.stdin.readline())

    lexer = Lexer(in)
    tokens = CommonTokenStream(lexer)
    parser = Parser(tokens)
    tree = parser.prog()

    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main(sys.argv)
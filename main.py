# Ping Pong Club Python file

# --- IMPORTS ---
import sys
from antlr4 import *
from antlr4.tree.Trees import Trees #Tree visualization in text
from poplLexer import poplLexer
from poplParser import poplParser

# --- MAIN ---
def main(argv):
    if len(sys.argv) > 1:
        io_stream = FileStream(sys.argv[1])
    else:
        io_stream = InputStream(sys.stdin.readline())

    lexer = poplLexer(io_stream)
    tokens = CommonTokenStream(lexer)
    parser = poplParser(tokens)
    tree = parser.start()

    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main(sys.argv)

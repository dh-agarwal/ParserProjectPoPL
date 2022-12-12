# Ping Pong Club Python file

# --- IMPORTS ---
from shutil import which
import sys
from antlr4 import *
from antlr4.tree.Trees import Trees #Tree visualization in text
from poplLexer import poplLexer
from poplParser import poplParser
import subprocess

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
    print('')

    p = subprocess.Popen([which("java"), '-cp', 'antlr-4.11.1-complete.jar', 'org.antlr.v4.gui.Interpreter', 'popl.g4', 'start', '-gui'])
    out, err = p.communicate()
    out = out.decode("UTF-8")
    err = err.decode("UTF-8")

    if err: print(err, end='')
    if out: print(out, end='')


if __name__ == "__main__":
    main(sys.argv)

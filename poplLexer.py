# Generated from popl.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\6\16?\n\16\r\16")
        buf.write("\16\16@\3\17\6\17D\n\17\r\17\16\17E\3\20\6\20I\n\20\r")
        buf.write("\20\16\20J\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2\5\5\2\62;C\\")
        buf.write("c|\3\2\f\f\3\2\62;\2N\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!")
        buf.write("\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2")
        buf.write("\r+\3\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25\64")
        buf.write("\3\2\2\2\27\67\3\2\2\2\31:\3\2\2\2\33>\3\2\2\2\35C\3\2")
        buf.write("\2\2\37H\3\2\2\2!\"\7,\2\2\"\4\3\2\2\2#$\7\61\2\2$\6\3")
        buf.write("\2\2\2%&\7-\2\2&\b\3\2\2\2\'(\7/\2\2(\n\3\2\2\2)*\7\'")
        buf.write("\2\2*\f\3\2\2\2+,\7*\2\2,\16\3\2\2\2-.\7+\2\2.\20\3\2")
        buf.write("\2\2/\60\7?\2\2\60\22\3\2\2\2\61\62\7-\2\2\62\63\7?\2")
        buf.write("\2\63\24\3\2\2\2\64\65\7/\2\2\65\66\7?\2\2\66\26\3\2\2")
        buf.write("\2\678\7,\2\289\7?\2\29\30\3\2\2\2:;\7\61\2\2;<\7?\2\2")
        buf.write("<\32\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@")
        buf.write("A\3\2\2\2A\34\3\2\2\2BD\t\3\2\2CB\3\2\2\2DE\3\2\2\2EC")
        buf.write("\3\2\2\2EF\3\2\2\2F\36\3\2\2\2GI\t\4\2\2HG\3\2\2\2IJ\3")
        buf.write("\2\2\2JH\3\2\2\2JK\3\2\2\2K \3\2\2\2\6\2@EJ\2")
        return buf.getvalue()


class poplLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    VAR = 13
    NEWLINE = 14
    INT = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'%'", "'('", "')'", "'='", "'+='", 
            "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "NEWLINE", "INT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "VAR", "NEWLINE", 
                  "INT" ]

    grammarFileName = "popl.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



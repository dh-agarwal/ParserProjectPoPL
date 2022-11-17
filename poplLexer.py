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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\6\16")
        buf.write("A\n\16\r\16\16\16B\3\17\6\17F\n\17\r\17\16\17G\3\20\6")
        buf.write("\20K\n\20\r\20\16\20L\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21a\n\21\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22\3\2\6\3\2\62;\5\2\62;C\\c|\3\2\f\f\4\2>>@@\2m\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3")
        buf.write("\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17")
        buf.write("/\3\2\2\2\21\61\3\2\2\2\23\63\3\2\2\2\25\66\3\2\2\2\27")
        buf.write("9\3\2\2\2\31<\3\2\2\2\33@\3\2\2\2\35E\3\2\2\2\37J\3\2")
        buf.write("\2\2!N\3\2\2\2#$\7,\2\2$\4\3\2\2\2%&\7\61\2\2&\6\3\2\2")
        buf.write("\2\'(\7-\2\2(\b\3\2\2\2)*\7/\2\2*\n\3\2\2\2+,\7\'\2\2")
        buf.write(",\f\3\2\2\2-.\7*\2\2.\16\3\2\2\2/\60\7+\2\2\60\20\3\2")
        buf.write("\2\2\61\62\7?\2\2\62\22\3\2\2\2\63\64\7-\2\2\64\65\7?")
        buf.write("\2\2\65\24\3\2\2\2\66\67\7/\2\2\678\7?\2\28\26\3\2\2\2")
        buf.write("9:\7,\2\2:;\7?\2\2;\30\3\2\2\2<=\7\61\2\2=>\7?\2\2>\32")
        buf.write("\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2")
        buf.write("\2\2C\34\3\2\2\2DF\t\3\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2")
        buf.write("\2GH\3\2\2\2H\36\3\2\2\2IK\t\4\2\2JI\3\2\2\2KL\3\2\2\2")
        buf.write("LJ\3\2\2\2LM\3\2\2\2M \3\2\2\2N`\5\35\17\2OP\7?\2\2Pa")
        buf.write("\7?\2\2QR\7@\2\2Ra\7?\2\2ST\7>\2\2Ta\7?\2\2Ua\t\5\2\2")
        buf.write("VW\7#\2\2Wa\7?\2\2XY\7c\2\2YZ\7p\2\2Za\7f\2\2[\\\7q\2")
        buf.write("\2\\a\7t\2\2]^\7p\2\2^_\7q\2\2_a\7v\2\2`O\3\2\2\2`Q\3")
        buf.write("\2\2\2`S\3\2\2\2`U\3\2\2\2`V\3\2\2\2`X\3\2\2\2`[\3\2\2")
        buf.write("\2`]\3\2\2\2ab\3\2\2\2bc\5\35\17\2c\"\3\2\2\2\7\2BGL`")
        buf.write("\2")
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
    INT = 13
    VAR = 14
    NEWLINE = 15
    IF = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'%'", "'('", "')'", "'='", "'+='", 
            "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>",
            "INT", "VAR", "NEWLINE", "IF" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "INT", "VAR", 
                  "NEWLINE", "IF" ]

    grammarFileName = "popl.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



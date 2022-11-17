# Generated from popl.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\7\2\16")
        buf.write("\n\2\f\2\16\2\21\13\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2")
        buf.write("\31\13\2\5\2\33\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n")
        buf.write("\3\3\3\3\3\3\3\7\3)\n\3\f\3\16\3,\13\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\2\3\4\6\2\4\6\b\2\4\3\2\3\7\3\2\n")
        buf.write("\16\2\67\2\32\3\2\2\2\4#\3\2\2\2\6-\3\2\2\2\b\61\3\2\2")
        buf.write("\2\n\13\5\6\4\2\13\f\7\21\2\2\f\16\3\2\2\2\r\n\3\2\2\2")
        buf.write("\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\33\3\2\2")
        buf.write("\2\21\17\3\2\2\2\22\23\5\b\5\2\23\24\7\21\2\2\24\26\3")
        buf.write("\2\2\2\25\22\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\32\17\3\2\2\2\32")
        buf.write("\27\3\2\2\2\33\3\3\2\2\2\34\35\b\3\1\2\35$\7\17\2\2\36")
        buf.write("$\7\20\2\2\37 \7\b\2\2 !\5\4\3\2!\"\7\t\2\2\"$\3\2\2\2")
        buf.write("#\34\3\2\2\2#\36\3\2\2\2#\37\3\2\2\2$*\3\2\2\2%&\f\6\2")
        buf.write("\2&\'\t\2\2\2\')\5\4\3\7(%\3\2\2\2),\3\2\2\2*(\3\2\2\2")
        buf.write("*+\3\2\2\2+\5\3\2\2\2,*\3\2\2\2-.\5\4\3\2./\t\2\2\2/\60")
        buf.write("\5\4\3\2\60\7\3\2\2\2\61\62\7\20\2\2\62\63\t\3\2\2\63")
        buf.write("\64\5\4\3\2\64\t\3\2\2\2\7\17\27\32#*")
        return buf.getvalue()


class poplParser ( Parser ):

    grammarFileName = "popl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'%'", "'('", 
                     "')'", "'='", "'+='", "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "VAR", "NEWLINE", "IF" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_fexpr = 2
    RULE_assign = 3

    ruleNames =  [ "start", "expr", "fexpr", "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    INT=13
    VAR=14
    NEWLINE=15
    IF=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poplParser.FexprContext)
            else:
                return self.getTypedRuleContext(poplParser.FexprContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(poplParser.NEWLINE)
            else:
                return self.getToken(poplParser.NEWLINE, i)

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poplParser.AssignContext)
            else:
                return self.getTypedRuleContext(poplParser.AssignContext,i)


        def getRuleIndex(self):
            return poplParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = poplParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << poplParser.T__5) | (1 << poplParser.INT) | (1 << poplParser.VAR))) != 0):
                    self.state = 8
                    self.fexpr()
                    self.state = 9
                    self.match(poplParser.NEWLINE)
                    self.state = 15
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==poplParser.VAR:
                    self.state = 16
                    self.assign()
                    self.state = 17
                    self.match(poplParser.NEWLINE)
                    self.state = 23
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(poplParser.INT, 0)

        def VAR(self):
            return self.getToken(poplParser.VAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poplParser.ExprContext)
            else:
                return self.getTypedRuleContext(poplParser.ExprContext,i)


        def getRuleIndex(self):
            return poplParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = poplParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [poplParser.INT]:
                self.state = 27
                self.match(poplParser.INT)
                pass
            elif token in [poplParser.VAR]:
                self.state = 28
                self.match(poplParser.VAR)
                pass
            elif token in [poplParser.T__5]:
                self.state = 29
                self.match(poplParser.T__5)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(poplParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = poplParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 35
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 36
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << poplParser.T__0) | (1 << poplParser.T__1) | (1 << poplParser.T__2) | (1 << poplParser.T__3) | (1 << poplParser.T__4))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 37
                    self.expr(5) 
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poplParser.ExprContext)
            else:
                return self.getTypedRuleContext(poplParser.ExprContext,i)


        def getRuleIndex(self):
            return poplParser.RULE_fexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFexpr" ):
                listener.enterFexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFexpr" ):
                listener.exitFexpr(self)




    def fexpr(self):

        localctx = poplParser.FexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.expr(0)
            self.state = 44
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << poplParser.T__0) | (1 << poplParser.T__1) | (1 << poplParser.T__2) | (1 << poplParser.T__3) | (1 << poplParser.T__4))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 45
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(poplParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(poplParser.ExprContext,0)


        def getRuleIndex(self):
            return poplParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = poplParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(poplParser.VAR)
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << poplParser.T__7) | (1 << poplParser.T__8) | (1 << poplParser.T__9) | (1 << poplParser.T__10) | (1 << poplParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 49
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         





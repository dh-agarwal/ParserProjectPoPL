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
        buf.write("\60\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2")
        buf.write("\16\2\17\13\2\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2")
        buf.write("\5\2\31\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\3")
        buf.write("\3\3\3\3\7\3\'\n\3\f\3\16\3*\13\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\2\3\4\5\2\4\6\2\4\3\2\3\7\3\2\n\16\2\62\2\30\3\2\2\2")
        buf.write("\4!\3\2\2\2\6+\3\2\2\2\b\t\5\4\3\2\t\n\7\21\2\2\n\f\3")
        buf.write("\2\2\2\13\b\3\2\2\2\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2")
        buf.write("\2\2\16\31\3\2\2\2\17\r\3\2\2\2\20\21\5\6\4\2\21\22\7")
        buf.write("\21\2\2\22\24\3\2\2\2\23\20\3\2\2\2\24\27\3\2\2\2\25\23")
        buf.write("\3\2\2\2\25\26\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\30")
        buf.write("\r\3\2\2\2\30\25\3\2\2\2\31\3\3\2\2\2\32\33\b\3\1\2\33")
        buf.write("\"\7\17\2\2\34\"\7\20\2\2\35\36\7\b\2\2\36\37\5\4\3\2")
        buf.write("\37 \7\t\2\2 \"\3\2\2\2!\32\3\2\2\2!\34\3\2\2\2!\35\3")
        buf.write("\2\2\2\"(\3\2\2\2#$\f\6\2\2$%\t\2\2\2%\'\5\4\3\7&#\3\2")
        buf.write("\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\5\3\2\2\2*(\3\2\2")
        buf.write("\2+,\7\20\2\2,-\t\3\2\2-.\5\4\3\2.\7\3\2\2\2\7\r\25\30")
        buf.write("!(")
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
    RULE_assign = 2

    ruleNames =  [ "start", "expr", "assign" ]

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(poplParser.ExprContext)
            else:
                return self.getTypedRuleContext(poplParser.ExprContext,i)


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
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << poplParser.T__5) | (1 << poplParser.INT) | (1 << poplParser.VAR))) != 0):
                    self.state = 6
                    self.expr(0)
                    self.state = 7
                    self.match(poplParser.NEWLINE)
                    self.state = 13
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==poplParser.VAR:
                    self.state = 14
                    self.assign()
                    self.state = 15
                    self.match(poplParser.NEWLINE)
                    self.state = 21
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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [poplParser.INT]:
                self.state = 25
                self.match(poplParser.INT)
                pass
            elif token in [poplParser.VAR]:
                self.state = 26
                self.match(poplParser.VAR)
                pass
            elif token in [poplParser.T__5]:
                self.state = 27
                self.match(poplParser.T__5)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(poplParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = poplParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 33
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 34
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << poplParser.T__0) | (1 << poplParser.T__1) | (1 << poplParser.T__2) | (1 << poplParser.T__3) | (1 << poplParser.T__4))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 35
                    self.expr(5) 
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 4, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(poplParser.VAR)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << poplParser.T__7) | (1 << poplParser.T__8) | (1 << poplParser.T__9) | (1 << poplParser.T__10) | (1 << poplParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 43
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
         





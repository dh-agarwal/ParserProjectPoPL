# Generated from popl.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .poplParser import poplParser
else:
    from poplParser import poplParser

# This class defines a complete listener for a parse tree produced by poplParser.
class poplListener(ParseTreeListener):

    # Enter a parse tree produced by poplParser#start.
    def enterStart(self, ctx:poplParser.StartContext):
        pass

    # Exit a parse tree produced by poplParser#start.
    def exitStart(self, ctx:poplParser.StartContext):
        pass


    # Enter a parse tree produced by poplParser#expr.
    def enterExpr(self, ctx:poplParser.ExprContext):
        pass

    # Exit a parse tree produced by poplParser#expr.
    def exitExpr(self, ctx:poplParser.ExprContext):
        pass


    # Enter a parse tree produced by poplParser#fexpr.
    def enterFexpr(self, ctx:poplParser.FexprContext):
        pass

    # Exit a parse tree produced by poplParser#fexpr.
    def exitFexpr(self, ctx:poplParser.FexprContext):
        pass


    # Enter a parse tree produced by poplParser#assign.
    def enterAssign(self, ctx:poplParser.AssignContext):
        pass

    # Exit a parse tree produced by poplParser#assign.
    def exitAssign(self, ctx:poplParser.AssignContext):
        pass



del poplParser
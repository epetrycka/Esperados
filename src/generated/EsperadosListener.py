# Generated from ../Grammar/Esperados.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EsperadosParser import EsperadosParser
else:
    from EsperadosParser import EsperadosParser

# This class defines a complete listener for a parse tree produced by EsperadosParser.
class EsperadosListener(ParseTreeListener):

    # Enter a parse tree produced by EsperadosParser#program.
    def enterProgram(self, ctx:EsperadosParser.ProgramContext):
        pass

    # Exit a parse tree produced by EsperadosParser#program.
    def exitProgram(self, ctx:EsperadosParser.ProgramContext):
        pass


    # Enter a parse tree produced by EsperadosParser#action.
    def enterAction(self, ctx:EsperadosParser.ActionContext):
        pass

    # Exit a parse tree produced by EsperadosParser#action.
    def exitAction(self, ctx:EsperadosParser.ActionContext):
        pass


    # Enter a parse tree produced by EsperadosParser#expr.
    def enterExpr(self, ctx:EsperadosParser.ExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#expr.
    def exitExpr(self, ctx:EsperadosParser.ExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#printExpr.
    def enterPrintExpr(self, ctx:EsperadosParser.PrintExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#printExpr.
    def exitPrintExpr(self, ctx:EsperadosParser.PrintExprContext):
        pass



del EsperadosParser
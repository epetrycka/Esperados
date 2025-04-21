# Generated from ../Grammar/Esperando.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EsperandoParser import EsperandoParser
else:
    from EsperandoParser import EsperandoParser

# This class defines a complete listener for a parse tree produced by EsperandoParser.
class EsperandoListener(ParseTreeListener):

    # Enter a parse tree produced by EsperandoParser#program.
    def enterProgram(self, ctx:EsperandoParser.ProgramContext):
        pass

    # Exit a parse tree produced by EsperandoParser#program.
    def exitProgram(self, ctx:EsperandoParser.ProgramContext):
        pass


    # Enter a parse tree produced by EsperandoParser#action.
    def enterAction(self, ctx:EsperandoParser.ActionContext):
        pass

    # Exit a parse tree produced by EsperandoParser#action.
    def exitAction(self, ctx:EsperandoParser.ActionContext):
        pass


    # Enter a parse tree produced by EsperandoParser#expr.
    def enterExpr(self, ctx:EsperandoParser.ExprContext):
        pass

    # Exit a parse tree produced by EsperandoParser#expr.
    def exitExpr(self, ctx:EsperandoParser.ExprContext):
        pass


    # Enter a parse tree produced by EsperandoParser#printExpr.
    def enterPrintExpr(self, ctx:EsperandoParser.PrintExprContext):
        pass

    # Exit a parse tree produced by EsperandoParser#printExpr.
    def exitPrintExpr(self, ctx:EsperandoParser.PrintExprContext):
        pass



del EsperandoParser
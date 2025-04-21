# Generated from ../Grammar/Esperando.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EsperandoParser import EsperandoParser
else:
    from EsperandoParser import EsperandoParser

# This class defines a complete generic visitor for a parse tree produced by EsperandoParser.

class EsperandoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EsperandoParser#program.
    def visitProgram(self, ctx:EsperandoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperandoParser#action.
    def visitAction(self, ctx:EsperandoParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperandoParser#expr.
    def visitExpr(self, ctx:EsperandoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperandoParser#printExpr.
    def visitPrintExpr(self, ctx:EsperandoParser.PrintExprContext):
        return self.visitChildren(ctx)



del EsperandoParser
# Generated from ../Grammar/Esperados.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EsperadosParser import EsperadosParser
else:
    from EsperadosParser import EsperadosParser

# This class defines a complete generic visitor for a parse tree produced by EsperadosParser.

class EsperadosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EsperadosParser#program.
    def visitProgram(self, ctx:EsperadosParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#action.
    def visitAction(self, ctx:EsperadosParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#expr.
    def visitExpr(self, ctx:EsperadosParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#printExpr.
    def visitPrintExpr(self, ctx:EsperadosParser.PrintExprContext):
        return self.visitChildren(ctx)



del EsperadosParser
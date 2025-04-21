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


    # Visit a parse tree produced by EsperadosParser#comment.
    def visitComment(self, ctx:EsperadosParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#greeting.
    def visitGreeting(self, ctx:EsperadosParser.GreetingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#goodbye.
    def visitGoodbye(self, ctx:EsperadosParser.GoodbyeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#action.
    def visitAction(self, ctx:EsperadosParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#algebraExpr.
    def visitAlgebraExpr(self, ctx:EsperadosParser.AlgebraExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#addStrings.
    def visitAddStrings(self, ctx:EsperadosParser.AddStringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#boolExpr.
    def visitBoolExpr(self, ctx:EsperadosParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#expr.
    def visitExpr(self, ctx:EsperadosParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#printExpr.
    def visitPrintExpr(self, ctx:EsperadosParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#variableExpr.
    def visitVariableExpr(self, ctx:EsperadosParser.VariableExprContext):
        return self.visitChildren(ctx)



del EsperadosParser
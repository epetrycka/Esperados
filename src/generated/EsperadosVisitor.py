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


    # Visit a parse tree produced by EsperadosParser#goodbye.
    def visitGoodbye(self, ctx:EsperadosParser.GoodbyeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#instructions.
    def visitInstructions(self, ctx:EsperadosParser.InstructionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#action.
    def visitAction(self, ctx:EsperadosParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#printExpr.
    def visitPrintExpr(self, ctx:EsperadosParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#variableExpr.
    def visitVariableExpr(self, ctx:EsperadosParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#condition.
    def visitCondition(self, ctx:EsperadosParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#ifExpr.
    def visitIfExpr(self, ctx:EsperadosParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#elifExpr.
    def visitElifExpr(self, ctx:EsperadosParser.ElifExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#elseExpr.
    def visitElseExpr(self, ctx:EsperadosParser.ElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#expr.
    def visitExpr(self, ctx:EsperadosParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#orExpr.
    def visitOrExpr(self, ctx:EsperadosParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#andExpr.
    def visitAndExpr(self, ctx:EsperadosParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#notExpr.
    def visitNotExpr(self, ctx:EsperadosParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#comparisonExpr.
    def visitComparisonExpr(self, ctx:EsperadosParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#additionExpr.
    def visitAdditionExpr(self, ctx:EsperadosParser.AdditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#multiExpr.
    def visitMultiExpr(self, ctx:EsperadosParser.MultiExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#exponExpr.
    def visitExponExpr(self, ctx:EsperadosParser.ExponExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperadosParser#atom.
    def visitAtom(self, ctx:EsperadosParser.AtomContext):
        return self.visitChildren(ctx)



del EsperadosParser
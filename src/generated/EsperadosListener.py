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


    # Enter a parse tree produced by EsperadosParser#comment.
    def enterComment(self, ctx:EsperadosParser.CommentContext):
        pass

    # Exit a parse tree produced by EsperadosParser#comment.
    def exitComment(self, ctx:EsperadosParser.CommentContext):
        pass


    # Enter a parse tree produced by EsperadosParser#greeting.
    def enterGreeting(self, ctx:EsperadosParser.GreetingContext):
        pass

    # Exit a parse tree produced by EsperadosParser#greeting.
    def exitGreeting(self, ctx:EsperadosParser.GreetingContext):
        pass


    # Enter a parse tree produced by EsperadosParser#goodbye.
    def enterGoodbye(self, ctx:EsperadosParser.GoodbyeContext):
        pass

    # Exit a parse tree produced by EsperadosParser#goodbye.
    def exitGoodbye(self, ctx:EsperadosParser.GoodbyeContext):
        pass


    # Enter a parse tree produced by EsperadosParser#action.
    def enterAction(self, ctx:EsperadosParser.ActionContext):
        pass

    # Exit a parse tree produced by EsperadosParser#action.
    def exitAction(self, ctx:EsperadosParser.ActionContext):
        pass


    # Enter a parse tree produced by EsperadosParser#algebraExpr.
    def enterAlgebraExpr(self, ctx:EsperadosParser.AlgebraExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#algebraExpr.
    def exitAlgebraExpr(self, ctx:EsperadosParser.AlgebraExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#addStrings.
    def enterAddStrings(self, ctx:EsperadosParser.AddStringsContext):
        pass

    # Exit a parse tree produced by EsperadosParser#addStrings.
    def exitAddStrings(self, ctx:EsperadosParser.AddStringsContext):
        pass


    # Enter a parse tree produced by EsperadosParser#boolExpr.
    def enterBoolExpr(self, ctx:EsperadosParser.BoolExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#boolExpr.
    def exitBoolExpr(self, ctx:EsperadosParser.BoolExprContext):
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


    # Enter a parse tree produced by EsperadosParser#variableExpr.
    def enterVariableExpr(self, ctx:EsperadosParser.VariableExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#variableExpr.
    def exitVariableExpr(self, ctx:EsperadosParser.VariableExprContext):
        pass



del EsperadosParser
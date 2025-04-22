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


    # Enter a parse tree produced by EsperadosParser#instructions.
    def enterInstructions(self, ctx:EsperadosParser.InstructionsContext):
        pass

    # Exit a parse tree produced by EsperadosParser#instructions.
    def exitInstructions(self, ctx:EsperadosParser.InstructionsContext):
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


    # Enter a parse tree produced by EsperadosParser#condition.
    def enterCondition(self, ctx:EsperadosParser.ConditionContext):
        pass

    # Exit a parse tree produced by EsperadosParser#condition.
    def exitCondition(self, ctx:EsperadosParser.ConditionContext):
        pass


    # Enter a parse tree produced by EsperadosParser#expr.
    def enterExpr(self, ctx:EsperadosParser.ExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#expr.
    def exitExpr(self, ctx:EsperadosParser.ExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#orExpr.
    def enterOrExpr(self, ctx:EsperadosParser.OrExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#orExpr.
    def exitOrExpr(self, ctx:EsperadosParser.OrExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#andExpr.
    def enterAndExpr(self, ctx:EsperadosParser.AndExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#andExpr.
    def exitAndExpr(self, ctx:EsperadosParser.AndExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#notExpr.
    def enterNotExpr(self, ctx:EsperadosParser.NotExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#notExpr.
    def exitNotExpr(self, ctx:EsperadosParser.NotExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:EsperadosParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:EsperadosParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#additionExpr.
    def enterAdditionExpr(self, ctx:EsperadosParser.AdditionExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#additionExpr.
    def exitAdditionExpr(self, ctx:EsperadosParser.AdditionExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:EsperadosParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:EsperadosParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#exponentialExpr.
    def enterExponentialExpr(self, ctx:EsperadosParser.ExponentialExprContext):
        pass

    # Exit a parse tree produced by EsperadosParser#exponentialExpr.
    def exitExponentialExpr(self, ctx:EsperadosParser.ExponentialExprContext):
        pass


    # Enter a parse tree produced by EsperadosParser#atom.
    def enterAtom(self, ctx:EsperadosParser.AtomContext):
        pass

    # Exit a parse tree produced by EsperadosParser#atom.
    def exitAtom(self, ctx:EsperadosParser.AtomContext):
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
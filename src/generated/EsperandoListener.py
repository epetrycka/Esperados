# Generated from Esperando.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by EsperandoParser#statement.
    def enterStatement(self, ctx:EsperandoParser.StatementContext):
        pass

    # Exit a parse tree produced by EsperandoParser#statement.
    def exitStatement(self, ctx:EsperandoParser.StatementContext):
        pass


    # Enter a parse tree produced by EsperandoParser#greeting.
    def enterGreeting(self, ctx:EsperandoParser.GreetingContext):
        pass

    # Exit a parse tree produced by EsperandoParser#greeting.
    def exitGreeting(self, ctx:EsperandoParser.GreetingContext):
        pass


    # Enter a parse tree produced by EsperandoParser#goodbye.
    def enterGoodbye(self, ctx:EsperandoParser.GoodbyeContext):
        pass

    # Exit a parse tree produced by EsperandoParser#goodbye.
    def exitGoodbye(self, ctx:EsperandoParser.GoodbyeContext):
        pass


    # Enter a parse tree produced by EsperandoParser#printStmt.
    def enterPrintStmt(self, ctx:EsperandoParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by EsperandoParser#printStmt.
    def exitPrintStmt(self, ctx:EsperandoParser.PrintStmtContext):
        pass



del EsperandoParser
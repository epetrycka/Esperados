# Generated from Esperando.g4 by ANTLR 4.13.2
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


    # Visit a parse tree produced by EsperandoParser#statement.
    def visitStatement(self, ctx:EsperandoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperandoParser#greeting.
    def visitGreeting(self, ctx:EsperandoParser.GreetingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperandoParser#goodbye.
    def visitGoodbye(self, ctx:EsperandoParser.GoodbyeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EsperandoParser#printStmt.
    def visitPrintStmt(self, ctx:EsperandoParser.PrintStmtContext):
        return self.visitChildren(ctx)



del EsperandoParser
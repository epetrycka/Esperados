from generated.EsperandoVisitor import EsperandoVisitor
from generated.EsperandoParser import EsperandoParser

class EsperandoVisitorImpl(EsperandoVisitor):
    def visitProgram(self, ctx):
        for stmt in ctx.action():
            self.visit(stmt)

    def visitAction(self, ctx:EsperandoParser.ActionContext):
        return self.visit(ctx.printExpr())

    def visitExpr(self, ctx:EsperandoParser.ExprContext):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.INT():
            return int(ctx.INT().getText())
        return None

    def visitPrintExpr(self, ctx:EsperandoParser.PrintExprContext):
        expr_result = self.visit(ctx.expr())
        print(expr_result)
        return expr_result

    def visitGreeting(self, ctx):
        print("👋 Cześć!")

    def visitGoodbye(self, ctx):
        print("👋 Do zobaczenia!")
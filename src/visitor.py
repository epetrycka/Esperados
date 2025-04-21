from generated.EsperadosVisitor import EsperadosVisitor
from generated.EsperadosParser import EsperadosParser

class EsperadosVisitorImpl(EsperadosVisitor):
    def visitProgram(self, ctx):
        for stmt in ctx.action():
            self.visit(stmt)

    def visitAction(self, ctx:EsperadosParser.ActionContext):
        return self.visit(ctx.printExpr())

    def visitExpr(self, ctx:EsperadosParser.ExprContext):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.INT():
            return int(ctx.INT().getText())
        return None

    def visitPrintExpr(self, ctx:EsperadosParser.PrintExprContext):
        expr_result = self.visit(ctx.expr())
        print(expr_result)
        return expr_result

    def visitGreeting(self, ctx):
        print("👋 Cześć!")

    def visitGoodbye(self, ctx):
        print("👋 Do zobaczenia!")
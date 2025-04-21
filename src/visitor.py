from generated.EsperandoVisitor import EsperandoVisitor

class EsperandoVisitorImpl(EsperandoVisitor):
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitPrintStmt(self, ctx):
        text = ctx.STRING().getText().strip('"')
        print(text)

    def visitGreeting(self, ctx):
        print("👋 Cześć!")

    def visitGoodbye(self, ctx):
        print("👋 Do zobaczenia!")

from generated.EsperadosVisitor import EsperadosVisitor
from generated.EsperadosParser import EsperadosParser

class EsperadosVisitorImpl(EsperadosVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: EsperadosParser.ProgramContext):
        if ctx.GREETING():
            print("👋 Saluton!")
        return self.visit(ctx.instructions())

    def visitInstructions(self, ctx: EsperadosParser.InstructionsContext):
        for child in ctx.children:
            if isinstance(child, EsperadosParser.ActionContext):
                self.visit(child)
        if ctx.goodbye():
            self.visit(ctx.goodbye())

    def visitGoodbye(self, ctx: EsperadosParser.GoodbyeContext):
        print("👋 Adiau!")

    def visitAction(self, ctx: EsperadosParser.ActionContext):
        if ctx.printExpr():
            return self.visit(ctx.printExpr())
        elif ctx.variableExpr():
            return self.visit(ctx.variableExpr())
        elif ctx.condition():
            return self.visit(ctx.condition())
        return None
    
    def visitPrintExpr(self, ctx: EsperadosParser.PrintExprContext):
        printValue = ""
        if ctx.expr():    
            for i in range(0, len(ctx.expr())):
                value = self.visit(ctx.expr(i))
                printValue += str(value)
        
        print(printValue)
        return None

    def visitVariableExpr(self, ctx: EsperadosParser.VariableExprContext):
        if ctx.NAME() is not None:
            varName = ctx.NAME().getText()
            if ctx.expr():
                value = self.visitExpr(ctx.expr())

            self.variables[varName] = value
            return None
        return None
    
    def visitCondition(self, ctx: EsperadosParser.ConditionContext):
        condition = self.visitExpr(ctx.expr())
        if condition:
            self.visitInstructions(ctx.instructions())
        return None

    def visitExpr(self, ctx: EsperadosParser.ExprContext):
        return self.visitOrExpr(ctx.orExpr())
    
    def visitOrExpr(self, ctx: EsperadosParser.OrExprContext):
        value = False
        for i in range (0, len(ctx.andExpr())):
            value = value or self.visitAndExpr(ctx.andExpr(i))
        return value

    def visitAndExpr(self, ctx: EsperadosParser.AndExprContext):
        value = True
        for i in range (0, len(ctx.notExpr())):
            value = value and self.visitNotExpr(ctx.notExpr(i))
        return value
        
    def visitNotExpr(self, ctx: EsperadosParser.NotExprContext):
        if ctx.NOT():
            return self.visitNotExpr(ctx.notExpr())
        if ctx.comparisonExpr():
            return self.visitComparisonExpr(ctx.comparisonExpr())
    
    def visitComparisonExpr(self, ctx: EsperadosParser.ComparisonExprContext):
        value = self.visitAdditionExpr(ctx.additionExpr(0))

        for i in range(1, len(ctx.additionExpr())):
            additionExpr2 = self.visitAdditionExpr(ctx.additionExpr(i))

            if ctx.EQUAL():
                value = value == additionExpr2
            if ctx.INEQUAL():
                value = value != additionExpr2
            if ctx.GREATER():
                value = value > additionExpr2
            if ctx.LESS():
                value = value < additionExpr2
            if ctx.EGREATER():
                value = value >= additionExpr2
            if ctx.ELESS():
                value = value <= additionExpr2

        return value
    
    def visitAdditionExpr(self, ctx: EsperadosParser.AdditionExprContext):
        value = self.visitMultiplicationExpr(ctx.multiplicationExpr(0))

        for i in range(1, len(ctx.multiplicationExpr())):
            multiplicationExpr2 = self.visitMultiplicationExpr(ctx.multiplicationExpr(i))

            if ctx.ADD():
                value = value + multiplicationExpr2
            if ctx.SUB():
                value = value - multiplicationExpr2

        return value
    
    def visitMultiplicationExpr(self, ctx: EsperadosParser.MultiplicationExprContext):
        value = self.visitExponentialExpr(ctx.exponentialExpr(0))

        for i in range(1, len(ctx.exponentialExpr())):
            exponentialExpr2 = self.visitExponentialExpr(ctx.exponentialExpr(i))

            if ctx.MULT():
                value = value * exponentialExpr2
            if ctx.DIV():
                value = value / exponentialExpr2
            if ctx.MOD():
                value = value % exponentialExpr2

        return value
    
    def visitExponentialExpr(self, ctx: EsperadosParser.ExponentialExprContext):
            value = self.visitAtom(ctx.atom(0))

            for i in range(1, len(ctx.atom())):
                atom2 = self.visitAtom(ctx.atom(i))
                value = value ** atom2

            return value
    
    def visitAtom(self, ctx: EsperadosParser.AtomContext):
        if ctx.STRING():
            return self.visitString(ctx.STRING())
        elif ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.NAME():
            return self.variables[ctx.NAME().getText()]
        elif ctx.expr():
            return self.visitExpr(ctx.expr())
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False

    def visitString(self, token):
        text = token.getText()[1:-1]
        try:
            return bytes(text, "utf-8").decode("unicode_escape")
        except UnicodeDecodeError:
            return text
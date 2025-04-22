from generated.EsperadosVisitor import EsperadosVisitor
from generated.EsperadosParser import EsperadosParser

class EsperadosVisitorImpl(EsperadosVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: EsperadosParser.ProgramContext):
        return self.visit(ctx.greeting())

    def visitGreeting(self, ctx: EsperadosParser.GreetingContext):
        print("👋 Saluton!")
        for action in ctx.action():
            self.visit(action)
        if ctx.goodbye():
            self.visit(ctx.goodbye())

    def visitGoodbye(self, ctx: EsperadosParser.GoodbyeContext):
        print("👋 Adiau!")

    def visitAction(self, ctx: EsperadosParser.ActionContext):
        if ctx.printExpr() is not None:
            return self.visit(ctx.printExpr())
        elif ctx.variableExpr() is not None:
            return self.visit(ctx.variableExpr())
        return None

    def visitPrintExpr(self, ctx: EsperadosParser.PrintExprContext):
        printValue = ""
        if ctx.expr():    
            for i in range(0, len(ctx.expr())):
                value = self.visit(ctx.expr(i))
                printValue += str(value)
        if ctx.boolExpr():
            for i in range(0, len(ctx.boolExpr())):
                value = self.visit(ctx.boolExpr(i))
                printValue += str(value)
        
        print(printValue)
        return None

    def visitVariableExpr(self, ctx: EsperadosParser.VariableExprContext):
        if ctx.NAME() is not None:
            varName = ctx.NAME().getText()
            if ctx.expr():
                value = self.visitExpr(ctx.expr())
            if ctx.boolExpr():
                value = self.visitBoolExpr(ctx.boolExpr())

            self.variables[varName] = value
            return None
        return None
    
    def visitBoolExpr(self, ctx: EsperadosParser.BoolExprContext):
        value1 = self.visit(ctx.expr(0))
        value2 = self.visit(ctx.expr(1))

        if ctx.EQUAL():
            return value1 == value2
        if ctx.INEQUAL():
            return value1 != value2
        if ctx.GREATER():
            return value1 > value2
        if ctx.LESS():
            return value1 < value2
        if ctx.EGREATER():
            return value1 >= value2
        if ctx.ELESS():
            return value1 <= value2

    def visitAlgebraExpr(self, ctx: EsperadosParser.AlgebraExprContext):
        value1 = None
        value2 = None

        if ctx.INT(0):
            value1 = int(ctx.INT()[0].getText())
        if ctx.FLOAT(0):
            if value1:
                value2 = float(ctx.FLOAT(0).getText())
            else:
                value1 = float(ctx.FLOAT(0).getText())
        if ctx.NAME(0):
            if value1:
                value2 = self.variables[ctx.NAME(0).getText()]
            else:
                value1 = self.variables[ctx.NAME(0).getText()]
        
        if ctx.INT(1):
            value2 = int(ctx.INT(1).getText())
        if ctx.FLOAT(1):
            value2 = float(ctx.FLOAT(1).getText())
        if ctx.NAME(1):
            value2 = self.variables[ctx.NAME(1).getText()]
        
        if ctx.ADD():
            return value1 + value2
        if ctx.SUB():
            return value1 - value2
        if ctx.MULT():
            return value1 * value2
        if ctx.DIV():
            return value1 / value2
        if ctx.MOD():
            return value1 % value2
        if ctx.EXPON():
            return value1 ** value2
        
    def visitAddStrings(self, ctx: EsperadosParser.AddStringsContext):
        return (ctx.STRING(0).getText().strip('"') + ctx.STRING(1).getText().strip('"'))

    def visitExpr(self, ctx: EsperadosParser.ExprContext):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.NAME():
            return self.variables[ctx.NAME().getText()]
        elif ctx.algebraExpr():
            return self.visitAlgebraExpr(ctx.algebraExpr())
        elif ctx.addStrings():
            return self.visitAddStrings(ctx.addStrings())
        return None
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
    
    def visitBoolExpr(self, ctx: EsperadosParser.BoolExprContext, value1):
        value2 = self.visit(ctx.expr())

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

    def visitAlgebraExpr(self, ctx: EsperadosParser.AlgebraExprContext, value1):
        value2 = None
        
        if ctx.STRING():
            value2 = self.visitString(ctx.STRING())
        elif ctx.INT():
            value2 = int(ctx.INT().getText())
        elif ctx.FLOAT():
            value2 = float(ctx.FLOAT().getText())
        elif ctx.NAME():
            value2 = self.variables[ctx.NAME().getText()]
        
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
        
    def visitLogicExpr(self, ctx: EsperadosParser.LogicExprContext, value1):
        value2 = self.visit(ctx.expr())
        if ctx.AND():
            return value1 and value2
        if ctx.ORL():
            return value1 or value2
        
        return None
        
    def visitAddStrings(self, ctx: EsperadosParser.AddStringsContext):
        return (self.visitString(ctx.STRING(0)) + self.visitString(ctx.STRING(1)))

    def visitExpr(self, ctx: EsperadosParser.ExprContext):
        if ctx.STRING():
            value = self.visitString(ctx.STRING())
        elif ctx.INT():
            value = int(ctx.INT().getText())
        elif ctx.FLOAT():
            value = float(ctx.FLOAT().getText())
        elif ctx.NAME():
            value = self.variables[ctx.NAME().getText()]
        elif ctx.addStrings():
            value = self.visitAddStrings(ctx.addStrings())

        if ctx.addExpr():
            value = self.visitAddExpr(ctx.addExpr(), value)
        
        return value
    
    def visitAddExpr(self, ctx: EsperadosParser.AddExprContext, value):
        if ctx.algebraExpr():
            return self.visitAlgebraExpr(ctx.algebraExpr(), value)
        elif ctx.boolExpr():
            return self.visitBoolExpr(ctx.boolExpr(), value)
        elif ctx.logicExpr():
            return self.visitLogicExpr(ctx.logicExpr(), value)
        
        return None
    
    def visitString(self, token):
        text = token.getText()[1:-1]
        try:
            return bytes(text, "utf-8").decode("unicode_escape")
        except UnicodeDecodeError:
            return text
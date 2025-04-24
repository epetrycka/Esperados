from generated.EsperadosVisitor import EsperadosVisitor
from generated.EsperadosParser import EsperadosParser

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class EsperadosVisitorImpl(EsperadosVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.lists = {}

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
        elif ctx.forLoop():
            return self.visit(ctx.forLoop())
        elif ctx.whileLoop():
            return self.visit(ctx.whileLoop())
        elif ctx.functionDef():
            return self.visit(ctx.functionDef())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.deleteStmt():
            return self.visit(ctx.deleteStmt())
        elif ctx.defList():
            return self.visit(ctx.defList())

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
        if ctx.ifExpr():
            conditionPassed = self.visitIfExpr(ctx.ifExpr())
        if not conditionPassed:
            for i in range (0, len(ctx.elifExpr())):
                conditionElsePassed = self.visitElifExpr(ctx.elifExpr(i))
                if conditionElsePassed:
                    return None
            if ctx.elseExpr():
                return self.visit(ctx.elseExpr())
        return None
    
    def visitIfExpr(self, ctx: EsperadosParser.IfExprContext):
        condition = self.visitExpr(ctx.expr())
        if condition:
            self.visitInstructions(ctx.instructions())
        return condition
    
    def visitElifExpr(self, ctx: EsperadosParser.ElifExprContext):
        condition = self.visitExpr(ctx.expr())
        if condition:
            self.visitInstructions(ctx.instructions())
        return condition
    
    def visitElseExpr(self, ctx: EsperadosParser.ElseExprContext):
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
        value = self.visitMultiExpr(ctx.multiExpr(0))

        for i in range(1, len(ctx.multiExpr())):
            multiExpr2 = self.visitMultiExpr(ctx.multiExpr(i))

            if ctx.ADD():
                value = value + multiExpr2
            if ctx.SUB():
                value = value - multiExpr2

        return value
    
    def visitMultiExpr(self, ctx: EsperadosParser.MultiExprContext):
        value = self.visitExponExpr(ctx.exponExpr(0))

        for i in range(1, len(ctx.exponExpr())):
            exponExpr2 = self.visitExponExpr(ctx.exponExpr(i))

            if ctx.MULT():
                value = value * exponExpr2
            if ctx.DIV():
                value = value / exponExpr2
            if ctx.MOD():
                value = value % exponExpr2

        return value
    
    def visitExponExpr(self, ctx: EsperadosParser.ExponExprContext):
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
        
    def visitForLoop(self, ctx: EsperadosParser.ForLoopContext):
        var_name = ctx.NAME().getText()
        start = int(ctx.INT(0).getText())
        end = int(ctx.INT(1).getText())
        step = int(ctx.INT(2).getText()) if ctx.INT(2) else 1

        i = start
        while (step > 0 and i < end) or (step < 0 and i > end):
            self.variables[var_name] = i
            try:
                self.visitLoopInstructions(ctx.loopInstructions())
            except ContinueException:
                i += step
                continue
            except BreakException:
                break
            i += step
    
    def visitLoopInstructions(self, ctx: EsperadosParser.LoopInstructionsContext):
        for child in ctx.children:
            self.visit(child)

    def visitLoopAction(self, ctx: EsperadosParser.LoopActionContext):
        if ctx.action():
            return self.visitAction(ctx.action())
        elif ctx.BREAK():
            raise BreakException()
        elif ctx.CONTINUE():
            raise ContinueException()
        
        return None
    
    def visitWhileLoop(self, ctx: EsperadosParser.WhileLoopContext):
        while self.visitExpr(ctx.expr()):
            try:
                self.visitLoopInstructions(ctx.loopInstructions())
            except ContinueException:
                continue
            except BreakException:
                break
        return None

    def visitFunctionDef(self, ctx: EsperadosParser.FunctionDefContext):
        funName = ctx.NAME().getText()
        self.functions[funName] = {"params": {}, "instructions": None}
        if ctx.parameters():
            self.visitParameters(ctx.parameters(), funName)
        self.functions[funName]["instructions"] = ctx.funDefInstructions()
        return None

    def visitParameters(self, ctx: EsperadosParser.ParametersContext, funName: str):
        for i in range(0, len(ctx.NAME())):
            self.functions[funName]["params"][ctx.NAME(i).getText()] = None
        return None
    
    def visitFunDefInstructions(self, ctx: EsperadosParser.FunDefInstructionsContext):
        for child in ctx.children:
            try:
                self.visit(child)
            except ReturnException as e:
                return e.value
        return None

    def visitFunDefAction(self, ctx: EsperadosParser.FunDefActionContext):
        if ctx.action():
            return self.visitAction(ctx.action())
        if ctx.returnStmt():
            return self.visitReturnStmt(ctx.returnStmt())

    def visitFunctionCall(self, ctx: EsperadosParser.FunctionCallContext):
        fun_name = ctx.NAME(0).getText()
        for i in range(0, len(ctx.expr())):
            self.functions[fun_name]["params"][ctx.NAME(i+1).getText()] = self.visitExpr(ctx.expr(i))
        temp_variables = self.variables
        self.variables = self.functions[fun_name]["params"]
        value = self.visitFunDefInstructions(self.functions[fun_name]["instructions"])
        self.variables = temp_variables
        return value
    
    def visitReturnStmt(self, ctx: EsperadosParser.ReturnStmtContext):
        value = self.visitExpr(ctx.expr()) if ctx.expr() else None
        raise ReturnException(value)
    
    def visitDeleteStmt(self, ctx: EsperadosParser.DeleteStmtContext):
        _ = self.variables.pop(ctx.NAME().getText())
        return None
    
    def visitDefList(self, ctx: EsperadosParser.DefListContext):
        list_name = ctx.NAME()
        self.lists[list_name] = []
        for i in range(0, len(ctx.expr())):
            self.lists[list_name].append(ctx.expr(i))
        print(self.lists[list_name])
        return None
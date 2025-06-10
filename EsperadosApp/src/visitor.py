import warnings
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
    def raiseError(self, ctx, error_type, message):
        line = f"line {ctx.start.line}:" if ctx and ctx.start else ''
        instruction = ' '
        if ctx and ctx.children:
            for child in ctx.children:
                instruction += child.getText()
                instruction += ' '
        else:
            instruction = ctx.getText() if ctx else ''
        contents = (f'"{instruction}"' + "\n") if ctx else ''
        line_message =f"{line} {contents}"
        full_message = f"\033[91m{line_message}{message}\033[0m"
        raise error_type(full_message)

    def __init__(self, input_provider=None):
        self.global_vars = {}
        self.global_lists = {}
        self.global_dicts = {}
        self.functions = {}
        self.temp_vars = []
        self.temp_lists = []
        self.temp_dicts = []

        self.input_provider = input_provider or input

    def visitProgram(self, ctx: EsperadosParser.ProgramContext):
        if ctx.GREETING():
            print("👋 Saluton!")
        self.temp_vars.append({})
        self.temp_lists.append({})
        self.temp_dicts.append({})
        if ctx.instructions():
            for i in range(0, len(ctx.instructions())):
                for child in ctx.instructions(i).children:
                    self.visit(child)
        if ctx.GOODBYE():
            print("👋 Adiau!")
        return None

    def visitActions(self, ctx: EsperadosParser.ActionsContext):
        if ctx.BREAK():
            raise BreakException()
        elif ctx.CONTINUE():
            raise ContinueException()
        else:
            for child in ctx.instructions().children:
                self.visit(child)
            return None

    #Functions
    
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
            elif ctx.INPUT():
                value = self.input_provider()
            if ctx.GLOBAL():
                try:
                    _, _ = self.findTempVariable(ctx.NAME())
                    self.raiseError(ctx, ValueError, f"Variable name {varName} is already in use as temporary")
                except NameError:
                    self.global_vars[varName] = value
            else:
                try:
                    _, _ = self.findGlobalVariable(ctx.NAME())
                    self.raiseError(ctx, ValueError, f"Variable name {varName} is already in use as global")
                except NameError:
                    self.temp_vars[-1][varName] = value
            return None
        return None
    
    def visitVariableChange(self, ctx: EsperadosParser.VariableChangeContext):
        if ctx.NAME() is not None:
            varName = ctx.NAME().getText()
            if ctx.INPUT():
                value = self.input_provider()
            elif ctx.LS():
                try:
                    _, where = self.findVariable(ctx.NAME())
                except NameError:
                    self.raiseError(ctx, ValueError, f"Variable name {varName} is not defined")
                if (where is not self.temp_lists[-1]) and (where is not self.global_lists):
                    self.raiseError(ctx, ValueError, f"Variable {varName} type is not a list")
                where[varName] = []
                for i in range(0, len(ctx.expr())):
                    where[varName].append(self.visitExpr(ctx.expr(i)))
                return None
            elif ctx.LC() and ctx.COLON():
                try:
                    _, where = self.findVariable(ctx.NAME())
                except NameError:
                    self.raiseError(ctx, ValueError, f"Variable name {varName} is not defined")
                if( where is not self.temp_dicts[-1]) and (where is not self.global_dicts):
                    self.raiseError(ctx, ValueError, f"Variable {varName} type is not a dict")
                where[varName] = {}
                for i in range(0, len(ctx.expr())-1, 2):
                    where[varName][self.visitExpr(ctx.expr(i))] = self.visitExpr(ctx.expr(i+1))
                return None
            elif ctx.expr():
                value = self.visit(ctx.expr(0))
            try:
                _, where = self.findVariable(ctx.NAME())
                if where is not self.temp_vars[-1] and where is not self.global_vars:
                    self.raiseError(ctx, ValueError, f"Variable {varName} type is a dict or list")
                where[varName] = value
            except NameError:
                self.raiseError(ctx, ValueError, f"Variable name {varName} is not defined")
            return None
        return None
    
    def visitDeleteStmt(self, ctx: EsperadosParser.DeleteStmtContext):
        _, where = self.findVariable(ctx.NAME())
        if where is not None:
            _ = where.pop(ctx.NAME().getText())
        return None
    
    def visitCondition(self, ctx: EsperadosParser.ConditionContext):
        self.temp_vars.append(self.temp_vars[-1].copy())
        if ctx.ifExpr():
            conditionPassed = self.visit(ctx.ifExpr())
        if not conditionPassed:
            for i in range (0, len(ctx.elifExpr())):
                conditionElsePassed = self.visit(ctx.elifExpr(i))
                if conditionElsePassed:
                    return None
            if ctx.elseExpr():
                    self.visit(ctx.elseExpr())
        _ = self.temp_vars.pop()
        return None
    
    def visitIfExpr(self, ctx: EsperadosParser.IfExprContext):
        condition = self.visit(ctx.expr())
        if condition:
            for i in range(0, len(ctx.actions())):
                self.visit(ctx.actions(i))
        return condition
    
    def visitElifExpr(self, ctx: EsperadosParser.ElifExprContext):
        condition = self.visit(ctx.expr())
        if condition:
            for i in range(0, len(ctx.actions())):
                self.visit(ctx.actions(i))
        return condition
    
    def visitElseExpr(self, ctx: EsperadosParser.ElseExprContext):
        for i in range(0, len(ctx.actions())):
                self.visit(ctx.actions(i))
        return None
    
    def visitForParam(self, ctx: EsperadosParser.ForParamContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.expr():
            value = self.visitExpr(ctx.expr())
            if isinstance(value, str):
                self.raiseError(ctx, ValueError, f"Value {value} is not a numberic type and cannot be used in for loop parameters")
            return value
    
    def visitForLoop(self, ctx: EsperadosParser.ForLoopContext):
        self.temp_vars.append(self.temp_vars[-1].copy())
        try:
            _, _ = self.findVariable(ctx.NAME())
            self.raiseError(ctx, ValueError, f"Variable name {ctx.NAME().getText()} is already in use")
        except NameError:
            var_name = ctx.NAME().getText()
        start = self.visit(ctx.forParam(0))
        end = self.visit(ctx.forParam(1))
        step = self.visit(ctx.forParam(2)) if ctx.forParam(2) else 1
        if (start < end and step < 0) or (start > end and step > 0) or step == 0:
            warnings.warn(f"Params start: {start}, end: {end}, step: {step} are not executable", RuntimeWarning)
        i = start
        while (step > 0 and i < end) or (step < 0 and i > end):
            self.temp_vars[-1][var_name] = i
            try:
                for k in range(0, len(ctx.actions())):
                    self.visit(ctx.actions(k))
            except ContinueException:
                i += step
                continue
            except BreakException:
                break
            i += step
        _ = self.temp_vars.pop()
        return None
    
    def visitWhileLoop(self, ctx: EsperadosParser.WhileLoopContext):
        self.temp_vars.append(self.temp_vars[-1].copy())
        while self.visitExpr(ctx.expr()):
            try:
                for k in range(0, len(ctx.actions())):
                    self.visit(ctx.actions(k))
            except ContinueException:
                continue
            except BreakException:
                break
        _ = self.temp_vars.pop()
        return None
    
    def visitForEachLoop(self, ctx: EsperadosParser.ForEachLoopContext):
        self.temp_vars.append(self.temp_vars[-1].copy())
        var_name = ctx.NAME(0).getText()
        lista, _ = self.findVariable(ctx.NAME(1))
        if not isinstance(lista, (list, str)):
            self.raiseError(ctx, ValueError, f"'Object {ctx.NAME(1)} is not iterable")
        for var in lista:
            self.temp_vars[-1][var_name] = var
            try:
                for k in range(0, len(ctx.actions())):
                    self.visit(ctx.actions(k))
            except ContinueException:
                continue
            except BreakException:
                break
        _ = self.temp_vars.pop()
        return None

    def visitFunctionDef(self, ctx: EsperadosParser.FunctionDefContext):
        funName = ctx.NAME().getText()
        if funName in self.functions:
            self.raiseError(ctx, NameError, f"Function {funName} is already defined")
        self.functions[funName] = {"params": {}, "instructions": None}
        if ctx.parameters():
            self.visitParameters(ctx.parameters(), funName)
        self.functions[funName]["instructions"] = ctx.actions()
        return None

    def visitParameters(self, ctx: EsperadosParser.ParametersContext, funName: str):
        for i in range(0, len(ctx.NAME())):
            if ctx.NAME(i).getText() in self.functions[funName]["params"]:
                self.raiseError(ctx, NameError, f"Parameter name '{ctx.NAME(i).getText()}' is already used in this function definition")
            self.functions[funName]["params"][ctx.NAME(i).getText()] = None
        return None

    def visitFunctionCall(self, ctx: EsperadosParser.FunctionCallContext):
        fun_name = ctx.NAME(0).getText()
        if fun_name in self.functions:
            function = self.functions[fun_name]
        elif fun_name in self.global_vars:
            function = self.global_vars[fun_name]
        elif fun_name in self.temp_vars[-1]:
            function = self.temp_vars[-1][fun_name]
        else:
            self.raiseError(ctx, NameError, f"Function '{fun_name}' is not defined.")
        self.temp_vars.append(self.temp_vars[-1].copy())
        value = None
        names = []
        for i in range(0, len(ctx.expr())):
            param_name = ctx.NAME(i+1).getText()
            if param_name in names:
                self.raiseError(ctx, NameError, f"Parameter {param_name} is redefined")
            names.append(param_name)
            if param_name not in function["params"]:
                self.raiseError(ctx, NameError, f"Parameter {param_name} does not apear in function definition")
            function["params"][param_name] = self.visit(ctx.expr(i))
        if any([function["params"][key] is None for key in function["params"].keys()]):
            missed_params = [key for key in function["params"].keys() if function["params"][key] is None]
            self.raiseError(ctx, NameError, f"Function require parameters: {missed_params}")
        self.temp_vars[-1].update(function["params"])
        instructions = function["instructions"]
        try:
            for i in range(0, len(instructions)):
                self.visit(instructions[i])
        except ReturnException as e:
            value = e.value
        _ = self.temp_vars.pop()
        for key in function["params"].keys():
            function["params"][key] = None
        return value
    
    def visitReturnStmt(self, ctx: EsperadosParser.ReturnStmtContext):
        value = self.visitExpr(ctx.expr()) if ctx.expr() else None
        raise ReturnException(value)
    
    def visitDefList(self, ctx: EsperadosParser.DefListContext):
        list_name = ctx.NAME().getText()
        if ctx.GLOBAL():
            self.global_lists[list_name] = []
            if ctx.getDictKeys():
                self.global_lists[list_name] = self.visit(ctx.getDictKeys())
            elif ctx.getDictValues():
                self.global_lists[list_name] = self.visit(ctx.getDictValues())
            else:
                for i in range(0, len(ctx.expr())):
                    self.global_lists[list_name].append(self.visitExpr(ctx.expr(i)))
        else:
            self.temp_lists[-1][list_name] = []
            if ctx.getDictKeys():
                self.temp_lists[-1][list_name] = self.visit(ctx.getDictKeys())
            elif ctx.getDictValues():
                self.temp_lists[-1][list_name] = self.visit(ctx.getDictValues())
            else:
                for i in range(0, len(ctx.expr())):
                    self.temp_lists[-1][list_name].append(self.visitExpr(ctx.expr(i)))
        return None

    def visitAddToList(self, ctx: EsperadosParser.AddToListContext):
        list_name = ctx.NAME().getText()
        value = self.visitExpr(ctx.expr())
        if list_name in self.global_lists:
            self.global_lists[list_name].append(value)
        elif list_name in self.temp_lists[-1].keys():
            self.temp_lists[-1][list_name].append(value)
        else:
            self.raiseError(ctx, NameError, f"List '{list_name}' is not defined")
        return None
    
    def visitRemoveFromList(self, ctx: EsperadosParser.RemoveFromListContext):
        list_name = ctx.NAME().getText()
        element = self.visitExpr(ctx.expr())
        if list_name in self.global_lists:
            if element not in self.global_lists[list_name]:
                self.raiseError(ctx, ValueError, f"Element '{element}' not found in list '{list_name}'")
            self.global_lists[list_name].remove(element)
        elif list_name in self.temp_lists[-1].keys():
            if element not in self.temp_lists[-1][list_name]:
                self.raiseError(ctx, ValueError, f"Element '{element}' not found in list '{list_name}'")
            self.temp_lists[-1][list_name].remove(element)
        else:
            if list_name not in self.global_lists or list_name not in self.temp_lists[-1].keys():
                self.raiseError(ctx, NameError, f"List '{list_name}' is not defined")
        return None
    
    def visitInsertToList(self, ctx: EsperadosParser.InsertToListContext):
        list_name = ctx.NAME().getText()
        index = self.visitExpr(ctx.expr(0))
        if isinstance(index, str):
            self.raiseError(ctx, ValueError, f"Index in insert function must be numeric")
        element = self.visitExpr(ctx.expr(1))
        if list_name in self.global_lists:
            self.global_lists[list_name].insert(index, element)
        elif list_name in self.temp_lists[-1].keys():
            self.temp_lists[-1][list_name].insert(index, element)
        else:
            if list_name not in self.global_lists or list_name not in self.temp_lists[-1].keys():
                self.raiseError(ctx, NameError, f"List '{list_name}' is not defined")
        return None
    
    def visitReplaceInStruct(self, ctx: EsperadosParser.ReplaceInStructContext):
        struct_name = ctx.NAME().getText()
        index = self.visitExpr(ctx.expr(0))
        element = self.visitExpr(ctx.expr(1))
        if struct_name in self.global_lists:
            if isinstance(index, str):
                self.raiseError(ctx, ValueError, f"Index in replace function must be numeric")
            if index < 0 or index > len(self.global_lists[struct_name]):
                self.raiseError(ctx, IndexError, f"List index out of range: {index}")
            self.global_lists[struct_name][index] = element
        elif struct_name in self.temp_lists[-1].keys():
            if isinstance(index, str):
                self.raiseError(ctx, ValueError, f"Index in replace function must be numeric")
            if index < 0 or index > len(self.temp_lists[-1][struct_name]):
                self.raiseError(ctx, IndexError, f"List index out of range: {index}")
            self.temp_lists[-1][struct_name][index] = element
        elif struct_name in self.global_dicts:
            self.global_dicts[struct_name][index] = element
        elif struct_name in self.temp_dicts[-1].keys():
            self.temp_dicts[-1][struct_name][index] = element
        else:
            if struct_name not in self.global_lists or struct_name not in self.temp_lists[-1].keys() and isinstance(index, int):
                self.raiseError(ctx, NameError, f"Struct '{struct_name}' is not defined")
        return None
    
    def visitDefDict(self, ctx: EsperadosParser.DefDictContext):
        dict_name = ctx.NAME().getText()
        new_dict = {}
        for i in range(0, len(ctx.expr())-1, 2):
            new_dict[self.visitExpr(ctx.expr(i))] = self.visitExpr(ctx.expr(i+1))
        if ctx.GLOBAL():
            self.global_dicts[dict_name] = new_dict
        else:
            self.temp_dicts[-1][dict_name] = new_dict
        del new_dict
        return None

    #Expressions
    
    def visitExpr(self, ctx: EsperadosParser.ExprContext):
        return self.visit(ctx.orExpr())
    
    def visitOrExpr(self, ctx: EsperadosParser.OrExprContext):
        value = False
        for i in range (0, len(ctx.andExpr())):
            value = value or self.visit(ctx.andExpr(i))
        return value

    def visitAndExpr(self, ctx: EsperadosParser.AndExprContext):
        value = True
        for i in range (0, len(ctx.notExpr())):
            value = value and self.visit(ctx.notExpr(i))
        return value
        
    def visitNotExpr(self, ctx: EsperadosParser.NotExprContext):
        if ctx.NOT():
            return not bool(self.visit(ctx.notExpr()))
        else:
            return self.visit(ctx.comparisonExpr())
    
    def visitComparisonExpr(self, ctx: EsperadosParser.ComparisonExprContext):
        value = self.visit(ctx.additionExpr(0))
        error = False
        for i in range(1, len(ctx.additionExpr())):
            additionExpr2 = self.visit(ctx.additionExpr(i))
            if ctx.EQUAL():
                value = value == additionExpr2
                return value
            if ctx.INEQUAL():
                value = value != additionExpr2
                return value
            if (isinstance(value, str) and isinstance(additionExpr2, str) == False) or (isinstance(additionExpr2, str) and isinstance(value, str) == False): 
                error = True
            elif (isinstance(value, list) and isinstance(additionExpr2, list) == False) or (isinstance(additionExpr2, list) and isinstance(value, list) == False):
                error = True
            elif (isinstance(value, dict) and isinstance(additionExpr2, dict) == False) or (isinstance(additionExpr2, dict) and isinstance(value, dict) == False):
                error = True
            if error:
                self.raiseError(ctx, TypeError, f"Can't compare '{type(value).__name__}' and '{type(additionExpr2).__name__}'")
            else:
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
        value = self.visit(ctx.multiExpr(0))
        error = False
        for i in range(1, len(ctx.multiExpr())):
            multiExpr2 = self.visit(ctx.multiExpr(i))
            if (isinstance(value, str) or isinstance(multiExpr2, str)) or (isinstance(value, list) and isinstance(multiExpr2, list)==False) or (isinstance(value, dict) and isinstance(multiExpr2, dict) == False):
                error = True
            elif (isinstance(multiExpr2, list) and isinstance(value, list)==False) or (isinstance(multiExpr2, dict) and isinstance(value, dict) == False):
                error = True
            if (isinstance(value, str) and isinstance(multiExpr2, str)):
                error = False
            if ctx.ADD():
                if (error):
                    self.raiseError(ctx, TypeError, f"Can't add types: {type(value).__name__} + {type(multiExpr2).__name__}")
                value = value + multiExpr2
            if ctx.SUB():
                if (isinstance(value, str) and isinstance(multiExpr2, str)):
                    error = True
                if (error):
                    self.raiseError(ctx, TypeError, f"Can't substract types: {type(value).__name__} - {type(multiExpr2).__name__}")
                value = value - multiExpr2
        return value
    
    def visitMultiExpr(self, ctx: EsperadosParser.MultiExprContext):
        value = self.visit(ctx.exponExpr(0))
        for i in range(1, len(ctx.exponExpr())):
            exponExpr2 = self.visit(ctx.exponExpr(i))
            if ctx.MULT():
                if not isinstance(value, (int, float)) or not isinstance(exponExpr2, (int, float)):
                    self.raiseError(ctx, TypeError, f"Can't multiply non-number types: {type(value).__name__} * {type(exponExpr2).__name__}")
                value = value * exponExpr2
            if ctx.DIV():
                if not isinstance(value, (int, float)) or not isinstance(exponExpr2, (int, float)):
                    self.raiseError(ctx, TypeError, f"Can't divide non-number types: {type(value).__name__} / {type(exponExpr2).__name__}")
                if exponExpr2 == 0:
                    self.raiseError(ctx, TypeError, "Division by zero is not allowed!")
                value = value / exponExpr2
            if ctx.MOD():
                if not isinstance(value, (int, float)) or not isinstance(exponExpr2, (int, float)):
                    self.raiseError(ctx, TypeError, f"Modulo operation requires numbers: {type(value).__name__} % {type(exponExpr2).__name__}")
                if exponExpr2 == 0:
                    self.raiseError(ctx, TypeError, "Modulo by zero is not allowed!")
                value = value % exponExpr2
        return value
    
    def visitExponExpr(self, ctx: EsperadosParser.ExponExprContext):
        value = self.visit(ctx.atom(0))
        for i in range(1, len(ctx.atom())):
            atom2 = self.visit(ctx.atom(i))
            if isinstance(value, (int, float)) == False or isinstance(atom2, (int, float)) == False:
                self.raiseError(ctx, TypeError, f"Cannot exponentiate non-numeric types: {type(value).__name__}, {type(atom2).__name__}")
            value = value ** atom2
        return value
    
    def visitAtom(self, ctx: EsperadosParser.AtomContext):
        if ctx.STRING():
            text = ctx.STRING().getText()[1:-1]
            try:
                return bytes(text, "utf-8").decode("unicode_escape")
            except UnicodeDecodeError:
                return text
        elif ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        elif ctx.getFromStruct():
            ctx = ctx.getFromStruct()
            struct_name = ctx.NAME().getText()
            index = self.visitExpr(ctx.expr())
            list_, dict_ = None, None
            if struct_name in self.global_lists:
                list_ = self.global_lists[struct_name]
            elif struct_name in self.temp_vars[-1].keys():
                list_ = self.temp_vars[-1][struct_name]
            elif struct_name in self.temp_lists[-1].keys():
                list_ = self.temp_lists[-1][struct_name]
            elif struct_name in self.global_dicts:
                dict_ = self.global_dicts[struct_name]
            elif struct_name in self.temp_dicts[-1].keys():
                dict_ = self.temp_dicts[-1][struct_name]
            else:
                if isinstance(index, int): self.raiseError(ctx, NameError, f"List '{struct_name}' is not defined")
                else: self.raiseError(ctx, NameError, f"Dict '{struct_name}' is not defined")
            if list_ and (index < 0 or index >= len(list_)):
                self.raiseError(ctx, IndexError, f"List index out of range. {struct_name} length: {len(list_)}")
            return list_[index] if list_ else dict_[index]
        elif ctx.NAME():
            value, _ = self.findVariable(ctx.NAME())
            return value
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.getDictKeys():
            self.visit(ctx.getDictKeys())
        elif ctx.getDictValues():
            self.visit(ctx.getDictValues())
        elif ctx.intValue():
            ctx = ctx.intValue()
            try:
                value = int(self.visit(ctx.expr()))
                return value
            except Exception:
                self.raiseError(ctx, ValueError, f"Cannot convert {self.visit(ctx.expr())} to int value")
        elif ctx.floatValue():
            ctx = ctx.floatValue()
            try:
                value = float(self.visit(ctx.expr()))
                return value
            except Exception:
                self.raiseError(ctx, ValueError, f"Cannot convert {self.visit(ctx.expr())} to float value")
        elif ctx.stringValue():
            ctx = ctx.stringValue()
            try:
                value = str(self.visit(ctx.expr()))
                return value
            except Exception:
                self.raiseError(ctx, ValueError, f"Cannot convert {self.visit(ctx.expr())} to string value")
        return None

    def visitGetDictKeys(self, ctx):
        dict_name = ctx.NAME().getText()
        if dict_name in self.global_dicts:
            return list(self.global_dicts[dict_name].keys())
        elif dict_name in self.temp_dicts[-1].keys():
            return list(self.temp_dicts[-1][dict_name].keys())
        else:
            self.raiseError(ctx, NameError, f"Dict '{dict_name}' is not defined")

    def visitGetDictValues(self, ctx):
        dict_name = ctx.NAME().getText()
        if dict_name in self.global_dicts:
            return list(self.global_dicts[dict_name].values())
        elif dict_name in self.temp_dicts[-1].keys():
            return list(self.temp_dicts[-1][dict_name].values())
        else:
            self.raiseError(ctx, NameError, f"Dict '{dict_name}' is not defined")

    #funkcja pomocnicza
          
    def findTempVariable(self, var_name):
        name = var_name.getText()
        if self.temp_vars and name in self.temp_vars[-1].keys():
            return (self.temp_vars[-1][name], self.temp_vars[-1])
        elif self.temp_lists and name in self.temp_lists[-1].keys():
            return (self.temp_lists[-1][name], self.temp_lists[-1])
        elif self.temp_dicts and name in self.temp_dicts[-1].keys():
            return (self.temp_dicts[-1][name], self.temp_dicts[-1])
        else:
            self.raiseError(None, NameError, f"Line {var_name.symbol.line}\n\tVariable '{name}' is not defined.")
        return (None, None)
        
    def findVariable(self, var_name):
        name = var_name.getText()
        if self.temp_vars and name in self.temp_vars[-1].keys():
            return (self.temp_vars[-1][name], self.temp_vars[-1])
        elif self.temp_lists and name in self.temp_lists[-1].keys():
            return (self.temp_lists[-1][name], self.temp_lists[-1])
        elif self.temp_dicts and name in self.temp_dicts[-1].keys():
            return (self.temp_dicts[-1][name], self.temp_dicts[-1])
        else:
            return self.findGlobalVariable(var_name)
    
    def findGlobalVariable(self, var_name):
        name = var_name.getText()
        if name in self.global_vars:
            return (self.global_vars[name], self.global_vars)
        elif name in self.global_lists:
            return (self.global_lists[name], self.global_lists)
        elif name in self.global_dicts:
            return (self.global_dicts[name], self.global_dicts)
        elif name in self.functions:
            return (self.functions[name], self.functions)
        else:
            self.raiseError(None, NameError, f"Line {var_name.symbol.line}\n\tVariable '{name}' is not defined.")
        return (None, None)
# Generated from ../Grammar/Esperados.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,
        1,2,1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,2,3,2,51,8,2,1,3,1,3,1,3,5,
        3,56,8,3,10,3,12,3,59,9,3,1,3,1,3,1,4,1,4,1,4,3,4,66,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,10,1,10,3,10,91,8,10,1,10,3,10,94,8,10,1,11,1,11,1,
        11,3,11,99,8,11,1,12,1,12,1,12,1,12,1,12,5,12,106,8,12,10,12,12,
        12,109,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,0,0,14,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,0,5,1,0,34,35,1,0,7,12,1,0,30,33,
        1,0,21,26,1,0,27,28,118,0,32,1,0,0,0,2,39,1,0,0,0,4,46,1,0,0,0,6,
        52,1,0,0,0,8,65,1,0,0,0,10,67,1,0,0,0,12,75,1,0,0,0,14,78,1,0,0,
        0,16,81,1,0,0,0,18,84,1,0,0,0,20,93,1,0,0,0,22,98,1,0,0,0,24,100,
        1,0,0,0,26,112,1,0,0,0,28,31,3,2,1,0,29,31,5,37,0,0,30,28,1,0,0,
        0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,
        1,0,0,0,34,32,1,0,0,0,35,36,5,1,0,0,36,37,3,4,2,0,37,38,5,0,0,1,
        38,1,1,0,0,0,39,40,7,0,0,0,40,3,1,0,0,0,41,45,3,2,1,0,42,45,3,8,
        4,0,43,45,5,37,0,0,44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,
        48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,
        0,49,51,3,6,3,0,50,49,1,0,0,0,50,51,1,0,0,0,51,5,1,0,0,0,52,57,5,
        2,0,0,53,56,3,2,1,0,54,56,5,37,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,
        59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,
        0,60,61,5,0,0,1,61,7,1,0,0,0,62,66,3,24,12,0,63,66,3,26,13,0,64,
        66,3,10,5,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,9,1,0,0,
        0,67,68,5,5,0,0,68,69,5,13,0,0,69,70,3,20,10,0,70,71,5,14,0,0,71,
        72,5,15,0,0,72,73,3,4,2,0,73,74,5,16,0,0,74,11,1,0,0,0,75,76,7,1,
        0,0,76,77,7,2,0,0,77,13,1,0,0,0,78,79,7,3,0,0,79,80,3,20,10,0,80,
        15,1,0,0,0,81,82,7,4,0,0,82,83,3,20,10,0,83,17,1,0,0,0,84,85,5,31,
        0,0,85,86,5,7,0,0,86,87,5,31,0,0,87,19,1,0,0,0,88,90,7,2,0,0,89,
        91,3,22,11,0,90,89,1,0,0,0,90,91,1,0,0,0,91,94,1,0,0,0,92,94,3,18,
        9,0,93,88,1,0,0,0,93,92,1,0,0,0,94,21,1,0,0,0,95,99,3,12,6,0,96,
        99,3,14,7,0,97,99,3,16,8,0,98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,
        0,0,99,23,1,0,0,0,100,101,5,3,0,0,101,102,5,13,0,0,102,107,3,20,
        10,0,103,104,5,17,0,0,104,106,3,20,10,0,105,103,1,0,0,0,106,109,
        1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,107,
        1,0,0,0,110,111,5,14,0,0,111,25,1,0,0,0,112,113,5,4,0,0,113,114,
        5,33,0,0,114,115,5,6,0,0,115,116,3,20,10,0,116,27,1,0,0,0,12,30,
        32,44,46,50,55,57,65,90,93,98,107
    ]

class EsperadosParser ( Parser ):

    grammarFileName = "Esperados.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Saluton'", "'Adiau'", "'skribi'", "'variablo'", 
                     "'se'", "'asigini'", "'aldoni'", "'subtrahi'", "'multigi'", 
                     "'dividi'", "'modulo'", "'intensigi'", "'('", "')'", 
                     "'{'", "'}'", "','", "'.'", "'vere'", "'malvero'", 
                     "'egala'", "'ne egala'", "'granda'", "'malgranda'", 
                     "'granda egala'", "'malgranda egala'", "'kaj'", "'au'", 
                     "'ne'" ]

    symbolicNames = [ "<INVALID>", "GREETING", "GOODBYE", "PRINT", "VARDEF", 
                      "IF", "ASS", "ADD", "SUB", "MULT", "DIV", "MOD", "EXPON", 
                      "LP", "RP", "LC", "RC", "COMMA", "DOT", "TRUE", "FALSE", 
                      "EQUAL", "INEQUAL", "GREATER", "LESS", "EGREATER", 
                      "ELESS", "AND", "OR", "NOT", "INT", "STRING", "FLOAT", 
                      "NAME", "COMMENT", "COMMENTBLOCK", "WS", "NL" ]

    RULE_program = 0
    RULE_comment = 1
    RULE_instructions = 2
    RULE_goodbye = 3
    RULE_action = 4
    RULE_condition = 5
    RULE_algebraExpr = 6
    RULE_boolExpr = 7
    RULE_logicExpr = 8
    RULE_addStrings = 9
    RULE_expr = 10
    RULE_addExpr = 11
    RULE_printExpr = 12
    RULE_variableExpr = 13

    ruleNames =  [ "program", "comment", "instructions", "goodbye", "action", 
                   "condition", "algebraExpr", "boolExpr", "logicExpr", 
                   "addStrings", "expr", "addExpr", "printExpr", "variableExpr" ]

    EOF = Token.EOF
    GREETING=1
    GOODBYE=2
    PRINT=3
    VARDEF=4
    IF=5
    ASS=6
    ADD=7
    SUB=8
    MULT=9
    DIV=10
    MOD=11
    EXPON=12
    LP=13
    RP=14
    LC=15
    RC=16
    COMMA=17
    DOT=18
    TRUE=19
    FALSE=20
    EQUAL=21
    INEQUAL=22
    GREATER=23
    LESS=24
    EGREATER=25
    ELESS=26
    AND=27
    OR=28
    NOT=29
    INT=30
    STRING=31
    FLOAT=32
    NAME=33
    COMMENT=34
    COMMENTBLOCK=35
    WS=36
    NL=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREETING(self):
            return self.getToken(EsperadosParser.GREETING, 0)

        def instructions(self):
            return self.getTypedRuleContext(EsperadosParser.InstructionsContext,0)


        def EOF(self):
            return self.getToken(EsperadosParser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.CommentContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.CommentContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.NL)
            else:
                return self.getToken(EsperadosParser.NL, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = EsperadosParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188978561024) != 0):
                self.state = 30
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 35]:
                    self.state = 28
                    self.comment()
                    pass
                elif token in [37]:
                    self.state = 29
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(EsperadosParser.GREETING)
            self.state = 36
            self.instructions()
            self.state = 37
            self.match(EsperadosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENTBLOCK(self):
            return self.getToken(EsperadosParser.COMMENTBLOCK, 0)

        def COMMENT(self):
            return self.getToken(EsperadosParser.COMMENT, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = EsperadosParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not(_la==34 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.CommentContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.CommentContext,i)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.ActionContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.ActionContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.NL)
            else:
                return self.getToken(EsperadosParser.NL, i)

        def goodbye(self):
            return self.getTypedRuleContext(EsperadosParser.GoodbyeContext,0)


        def getRuleIndex(self):
            return EsperadosParser.RULE_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructions" ):
                listener.enterInstructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructions" ):
                listener.exitInstructions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructions" ):
                return visitor.visitInstructions(self)
            else:
                return visitor.visitChildren(self)




    def instructions(self):

        localctx = EsperadosParser.InstructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188978561080) != 0):
                self.state = 44
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 35]:
                    self.state = 41
                    self.comment()
                    pass
                elif token in [3, 4, 5]:
                    self.state = 42
                    self.action()
                    pass
                elif token in [37]:
                    self.state = 43
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 49
                self.goodbye()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoodbyeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOODBYE(self):
            return self.getToken(EsperadosParser.GOODBYE, 0)

        def EOF(self):
            return self.getToken(EsperadosParser.EOF, 0)

        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.CommentContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.CommentContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.NL)
            else:
                return self.getToken(EsperadosParser.NL, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_goodbye

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoodbye" ):
                listener.enterGoodbye(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoodbye" ):
                listener.exitGoodbye(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoodbye" ):
                return visitor.visitGoodbye(self)
            else:
                return visitor.visitChildren(self)




    def goodbye(self):

        localctx = EsperadosParser.GoodbyeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_goodbye)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(EsperadosParser.GOODBYE)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188978561024) != 0):
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 35]:
                    self.state = 53
                    self.comment()
                    pass
                elif token in [37]:
                    self.state = 54
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(EsperadosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printExpr(self):
            return self.getTypedRuleContext(EsperadosParser.PrintExprContext,0)


        def variableExpr(self):
            return self.getTypedRuleContext(EsperadosParser.VariableExprContext,0)


        def condition(self):
            return self.getTypedRuleContext(EsperadosParser.ConditionContext,0)


        def getRuleIndex(self):
            return EsperadosParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = EsperadosParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 62
                self.printExpr()
                pass
            elif token in [4]:
                self.state = 63
                self.variableExpr()
                pass
            elif token in [5]:
                self.state = 64
                self.condition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(EsperadosParser.IF, 0)

        def LP(self):
            return self.getToken(EsperadosParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

        def LC(self):
            return self.getToken(EsperadosParser.LC, 0)

        def instructions(self):
            return self.getTypedRuleContext(EsperadosParser.InstructionsContext,0)


        def RC(self):
            return self.getToken(EsperadosParser.RC, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = EsperadosParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(EsperadosParser.IF)
            self.state = 68
            self.match(EsperadosParser.LP)
            self.state = 69
            self.expr()
            self.state = 70
            self.match(EsperadosParser.RP)
            self.state = 71
            self.match(EsperadosParser.LC)
            self.state = 72
            self.instructions()
            self.state = 73
            self.match(EsperadosParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlgebraExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(EsperadosParser.ADD, 0)

        def SUB(self):
            return self.getToken(EsperadosParser.SUB, 0)

        def MULT(self):
            return self.getToken(EsperadosParser.MULT, 0)

        def DIV(self):
            return self.getToken(EsperadosParser.DIV, 0)

        def MOD(self):
            return self.getToken(EsperadosParser.MOD, 0)

        def EXPON(self):
            return self.getToken(EsperadosParser.EXPON, 0)

        def INT(self):
            return self.getToken(EsperadosParser.INT, 0)

        def FLOAT(self):
            return self.getToken(EsperadosParser.FLOAT, 0)

        def NAME(self):
            return self.getToken(EsperadosParser.NAME, 0)

        def STRING(self):
            return self.getToken(EsperadosParser.STRING, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_algebraExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlgebraExpr" ):
                listener.enterAlgebraExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlgebraExpr" ):
                listener.exitAlgebraExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlgebraExpr" ):
                return visitor.visitAlgebraExpr(self)
            else:
                return visitor.visitChildren(self)




    def algebraExpr(self):

        localctx = EsperadosParser.AlgebraExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_algebraExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8064) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


        def EQUAL(self):
            return self.getToken(EsperadosParser.EQUAL, 0)

        def INEQUAL(self):
            return self.getToken(EsperadosParser.INEQUAL, 0)

        def GREATER(self):
            return self.getToken(EsperadosParser.GREATER, 0)

        def LESS(self):
            return self.getToken(EsperadosParser.LESS, 0)

        def EGREATER(self):
            return self.getToken(EsperadosParser.EGREATER, 0)

        def ELESS(self):
            return self.getToken(EsperadosParser.ELESS, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)




    def boolExpr(self):

        localctx = EsperadosParser.BoolExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_boolExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 79
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


        def AND(self):
            return self.getToken(EsperadosParser.AND, 0)

        def OR(self):
            return self.getToken(EsperadosParser.OR, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_logicExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicExpr" ):
                return visitor.visitLogicExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicExpr(self):

        localctx = EsperadosParser.LogicExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logicExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 82
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddStringsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.STRING)
            else:
                return self.getToken(EsperadosParser.STRING, i)

        def ADD(self):
            return self.getToken(EsperadosParser.ADD, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_addStrings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddStrings" ):
                listener.enterAddStrings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddStrings" ):
                listener.exitAddStrings(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddStrings" ):
                return visitor.visitAddStrings(self)
            else:
                return visitor.visitChildren(self)




    def addStrings(self):

        localctx = EsperadosParser.AddStringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_addStrings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(EsperadosParser.STRING)
            self.state = 85
            self.match(EsperadosParser.ADD)
            self.state = 86
            self.match(EsperadosParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addStrings(self):
            return self.getTypedRuleContext(EsperadosParser.AddStringsContext,0)


        def STRING(self):
            return self.getToken(EsperadosParser.STRING, 0)

        def INT(self):
            return self.getToken(EsperadosParser.INT, 0)

        def FLOAT(self):
            return self.getToken(EsperadosParser.FLOAT, 0)

        def NAME(self):
            return self.getToken(EsperadosParser.NAME, 0)

        def addExpr(self):
            return self.getTypedRuleContext(EsperadosParser.AddExprContext,0)


        def getRuleIndex(self):
            return EsperadosParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = EsperadosParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 88
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16106127360) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 534781824) != 0):
                    self.state = 89
                    self.addExpr()


                pass

            elif la_ == 2:
                self.state = 92
                self.addStrings()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def algebraExpr(self):
            return self.getTypedRuleContext(EsperadosParser.AlgebraExprContext,0)


        def boolExpr(self):
            return self.getTypedRuleContext(EsperadosParser.BoolExprContext,0)


        def logicExpr(self):
            return self.getTypedRuleContext(EsperadosParser.LogicExprContext,0)


        def getRuleIndex(self):
            return EsperadosParser.RULE_addExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)




    def addExpr(self):

        localctx = EsperadosParser.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_addExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11, 12]:
                self.state = 95
                self.algebraExpr()
                pass
            elif token in [21, 22, 23, 24, 25, 26]:
                self.state = 96
                self.boolExpr()
                pass
            elif token in [27, 28]:
                self.state = 97
                self.logicExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(EsperadosParser.PRINT, 0)

        def LP(self):
            return self.getToken(EsperadosParser.LP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.ExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.ExprContext,i)


        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.COMMA)
            else:
                return self.getToken(EsperadosParser.COMMA, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_printExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)




    def printExpr(self):

        localctx = EsperadosParser.PrintExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_printExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(EsperadosParser.PRINT)
            self.state = 101
            self.match(EsperadosParser.LP)
            self.state = 102
            self.expr()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 103
                self.match(EsperadosParser.COMMA)
                self.state = 104
                self.expr()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(EsperadosParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARDEF(self):
            return self.getToken(EsperadosParser.VARDEF, 0)

        def NAME(self):
            return self.getToken(EsperadosParser.NAME, 0)

        def ASS(self):
            return self.getToken(EsperadosParser.ASS, 0)

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


        def getRuleIndex(self):
            return EsperadosParser.RULE_variableExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)




    def variableExpr(self):

        localctx = EsperadosParser.VariableExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variableExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(EsperadosParser.VARDEF)
            self.state = 113
            self.match(EsperadosParser.NAME)
            self.state = 114
            self.match(EsperadosParser.ASS)
            self.state = 115
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






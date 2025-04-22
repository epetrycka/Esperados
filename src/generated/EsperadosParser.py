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
        4,1,37,166,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,5,0,37,8,0,10,0,12,0,40,9,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,
        2,1,2,3,2,57,8,2,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,
        1,4,1,4,1,4,3,4,72,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        7,1,7,1,7,5,7,87,8,7,10,7,12,7,90,9,7,1,8,1,8,1,8,5,8,95,8,8,10,
        8,12,8,98,9,8,1,9,1,9,1,9,3,9,103,8,9,1,10,1,10,1,10,5,10,108,8,
        10,10,10,12,10,111,9,10,1,11,1,11,1,11,5,11,116,8,11,10,11,12,11,
        119,9,11,1,12,1,12,1,12,5,12,124,8,12,10,12,12,12,127,9,12,1,13,
        1,13,1,13,5,13,132,8,13,10,13,12,13,135,9,13,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,147,8,14,1,15,1,15,1,15,1,15,
        1,15,5,15,154,8,15,10,15,12,15,157,9,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,0,4,1,0,34,35,1,0,21,26,1,0,7,8,1,0,9,11,172,0,38,1,0,0,0,2,45,
        1,0,0,0,4,52,1,0,0,0,6,58,1,0,0,0,8,71,1,0,0,0,10,73,1,0,0,0,12,
        81,1,0,0,0,14,83,1,0,0,0,16,91,1,0,0,0,18,102,1,0,0,0,20,104,1,0,
        0,0,22,112,1,0,0,0,24,120,1,0,0,0,26,128,1,0,0,0,28,146,1,0,0,0,
        30,148,1,0,0,0,32,160,1,0,0,0,34,37,3,2,1,0,35,37,5,37,0,0,36,34,
        1,0,0,0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,
        39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,1,0,0,42,43,3,4,2,0,43,44,5,
        0,0,1,44,1,1,0,0,0,45,46,7,0,0,0,46,3,1,0,0,0,47,51,3,2,1,0,48,51,
        3,8,4,0,49,51,5,37,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,
        51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,56,1,0,0,0,54,52,1,
        0,0,0,55,57,3,6,3,0,56,55,1,0,0,0,56,57,1,0,0,0,57,5,1,0,0,0,58,
        63,5,2,0,0,59,62,3,2,1,0,60,62,5,37,0,0,61,59,1,0,0,0,61,60,1,0,
        0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,
        1,0,0,0,66,67,5,0,0,1,67,7,1,0,0,0,68,72,3,30,15,0,69,72,3,32,16,
        0,70,72,3,10,5,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,9,
        1,0,0,0,73,74,5,5,0,0,74,75,5,13,0,0,75,76,3,12,6,0,76,77,5,14,0,
        0,77,78,5,15,0,0,78,79,3,4,2,0,79,80,5,16,0,0,80,11,1,0,0,0,81,82,
        3,14,7,0,82,13,1,0,0,0,83,88,3,16,8,0,84,85,5,28,0,0,85,87,3,16,
        8,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,15,
        1,0,0,0,90,88,1,0,0,0,91,96,3,18,9,0,92,93,5,27,0,0,93,95,3,18,9,
        0,94,92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,17,
        1,0,0,0,98,96,1,0,0,0,99,100,5,29,0,0,100,103,3,18,9,0,101,103,3,
        20,10,0,102,99,1,0,0,0,102,101,1,0,0,0,103,19,1,0,0,0,104,109,3,
        22,11,0,105,106,7,1,0,0,106,108,3,22,11,0,107,105,1,0,0,0,108,111,
        1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,21,1,0,0,0,111,109,1,
        0,0,0,112,117,3,24,12,0,113,114,7,2,0,0,114,116,3,24,12,0,115,113,
        1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,23,1,
        0,0,0,119,117,1,0,0,0,120,125,3,26,13,0,121,122,7,3,0,0,122,124,
        3,26,13,0,123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,25,1,0,0,0,127,125,1,0,0,0,128,133,3,28,14,0,129,130,
        5,12,0,0,130,132,3,28,14,0,131,129,1,0,0,0,132,135,1,0,0,0,133,131,
        1,0,0,0,133,134,1,0,0,0,134,27,1,0,0,0,135,133,1,0,0,0,136,137,5,
        13,0,0,137,138,3,12,6,0,138,139,5,14,0,0,139,147,1,0,0,0,140,147,
        5,30,0,0,141,147,5,32,0,0,142,147,5,31,0,0,143,147,5,19,0,0,144,
        147,5,20,0,0,145,147,5,33,0,0,146,136,1,0,0,0,146,140,1,0,0,0,146,
        141,1,0,0,0,146,142,1,0,0,0,146,143,1,0,0,0,146,144,1,0,0,0,146,
        145,1,0,0,0,147,29,1,0,0,0,148,149,5,3,0,0,149,150,5,13,0,0,150,
        155,3,12,6,0,151,152,5,17,0,0,152,154,3,12,6,0,153,151,1,0,0,0,154,
        157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,158,1,0,0,0,157,
        155,1,0,0,0,158,159,5,14,0,0,159,31,1,0,0,0,160,161,5,4,0,0,161,
        162,5,33,0,0,162,163,5,6,0,0,163,164,3,12,6,0,164,33,1,0,0,0,17,
        36,38,50,52,56,61,63,71,88,96,102,109,117,125,133,146,155
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
    RULE_expr = 6
    RULE_orExpr = 7
    RULE_andExpr = 8
    RULE_notExpr = 9
    RULE_comparisonExpr = 10
    RULE_additionExpr = 11
    RULE_multiplicationExpr = 12
    RULE_exponentialExpr = 13
    RULE_atom = 14
    RULE_printExpr = 15
    RULE_variableExpr = 16

    ruleNames =  [ "program", "comment", "instructions", "goodbye", "action", 
                   "condition", "expr", "orExpr", "andExpr", "notExpr", 
                   "comparisonExpr", "additionExpr", "multiplicationExpr", 
                   "exponentialExpr", "atom", "printExpr", "variableExpr" ]

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
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188978561024) != 0):
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 35]:
                    self.state = 34
                    self.comment()
                    pass
                elif token in [37]:
                    self.state = 35
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(EsperadosParser.GREETING)
            self.state = 42
            self.instructions()
            self.state = 43
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
            self.state = 45
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
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188978561080) != 0):
                self.state = 50
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 35]:
                    self.state = 47
                    self.comment()
                    pass
                elif token in [3, 4, 5]:
                    self.state = 48
                    self.action()
                    pass
                elif token in [37]:
                    self.state = 49
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 55
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
            self.state = 58
            self.match(EsperadosParser.GOODBYE)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 188978561024) != 0):
                self.state = 61
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [34, 35]:
                    self.state = 59
                    self.comment()
                    pass
                elif token in [37]:
                    self.state = 60
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
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
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 68
                self.printExpr()
                pass
            elif token in [4]:
                self.state = 69
                self.variableExpr()
                pass
            elif token in [5]:
                self.state = 70
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
            self.state = 73
            self.match(EsperadosParser.IF)
            self.state = 74
            self.match(EsperadosParser.LP)
            self.state = 75
            self.expr()
            self.state = 76
            self.match(EsperadosParser.RP)
            self.state = 77
            self.match(EsperadosParser.LC)
            self.state = 78
            self.instructions()
            self.state = 79
            self.match(EsperadosParser.RC)
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

        def orExpr(self):
            return self.getTypedRuleContext(EsperadosParser.OrExprContext,0)


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
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.orExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.AndExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.AndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.OR)
            else:
                return self.getToken(EsperadosParser.OR, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_orExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = EsperadosParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.andExpr()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 84
                self.match(EsperadosParser.OR)
                self.state = 85
                self.andExpr()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.NotExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.NotExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.AND)
            else:
                return self.getToken(EsperadosParser.AND, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_andExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = EsperadosParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.notExpr()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 92
                self.match(EsperadosParser.AND)
                self.state = 93
                self.notExpr()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(EsperadosParser.NOT, 0)

        def notExpr(self):
            return self.getTypedRuleContext(EsperadosParser.NotExprContext,0)


        def comparisonExpr(self):
            return self.getTypedRuleContext(EsperadosParser.ComparisonExprContext,0)


        def getRuleIndex(self):
            return EsperadosParser.RULE_notExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)




    def notExpr(self):

        localctx = EsperadosParser.NotExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_notExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 99
                self.match(EsperadosParser.NOT)
                self.state = 100
                self.notExpr()
                pass
            elif token in [13, 19, 20, 30, 31, 32, 33]:
                self.state = 101
                self.comparisonExpr()
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


    class ComparisonExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.AdditionExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.AdditionExprContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.EQUAL)
            else:
                return self.getToken(EsperadosParser.EQUAL, i)

        def INEQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.INEQUAL)
            else:
                return self.getToken(EsperadosParser.INEQUAL, i)

        def GREATER(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.GREATER)
            else:
                return self.getToken(EsperadosParser.GREATER, i)

        def LESS(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.LESS)
            else:
                return self.getToken(EsperadosParser.LESS, i)

        def EGREATER(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.EGREATER)
            else:
                return self.getToken(EsperadosParser.EGREATER, i)

        def ELESS(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.ELESS)
            else:
                return self.getToken(EsperadosParser.ELESS, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_comparisonExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)




    def comparisonExpr(self):

        localctx = EsperadosParser.ComparisonExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.additionExpr()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0):
                self.state = 105
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                self.additionExpr()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicationExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.MultiplicationExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.MultiplicationExprContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.ADD)
            else:
                return self.getToken(EsperadosParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.SUB)
            else:
                return self.getToken(EsperadosParser.SUB, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_additionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionExpr" ):
                listener.enterAdditionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionExpr" ):
                listener.exitAdditionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionExpr" ):
                return visitor.visitAdditionExpr(self)
            else:
                return visitor.visitChildren(self)




    def additionExpr(self):

        localctx = EsperadosParser.AdditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_additionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.multiplicationExpr()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 113
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 114
                self.multiplicationExpr()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponentialExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.ExponentialExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.ExponentialExprContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.MULT)
            else:
                return self.getToken(EsperadosParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.DIV)
            else:
                return self.getToken(EsperadosParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.MOD)
            else:
                return self.getToken(EsperadosParser.MOD, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_multiplicationExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpr" ):
                return visitor.visitMultiplicationExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicationExpr(self):

        localctx = EsperadosParser.MultiplicationExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_multiplicationExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.exponentialExpr()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                self.state = 121
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                self.exponentialExpr()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentialExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.AtomContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.AtomContext,i)


        def EXPON(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.EXPON)
            else:
                return self.getToken(EsperadosParser.EXPON, i)

        def getRuleIndex(self):
            return EsperadosParser.RULE_exponentialExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponentialExpr" ):
                listener.enterExponentialExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentialExpr" ):
                listener.exitExponentialExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponentialExpr" ):
                return visitor.visitExponentialExpr(self)
            else:
                return visitor.visitChildren(self)




    def exponentialExpr(self):

        localctx = EsperadosParser.ExponentialExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exponentialExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.atom()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 129
                self.match(EsperadosParser.EXPON)
                self.state = 130
                self.atom()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(EsperadosParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

        def INT(self):
            return self.getToken(EsperadosParser.INT, 0)

        def FLOAT(self):
            return self.getToken(EsperadosParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(EsperadosParser.STRING, 0)

        def TRUE(self):
            return self.getToken(EsperadosParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(EsperadosParser.FALSE, 0)

        def NAME(self):
            return self.getToken(EsperadosParser.NAME, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = EsperadosParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 136
                self.match(EsperadosParser.LP)
                self.state = 137
                self.expr()
                self.state = 138
                self.match(EsperadosParser.RP)
                pass
            elif token in [30]:
                self.state = 140
                self.match(EsperadosParser.INT)
                pass
            elif token in [32]:
                self.state = 141
                self.match(EsperadosParser.FLOAT)
                pass
            elif token in [31]:
                self.state = 142
                self.match(EsperadosParser.STRING)
                pass
            elif token in [19]:
                self.state = 143
                self.match(EsperadosParser.TRUE)
                pass
            elif token in [20]:
                self.state = 144
                self.match(EsperadosParser.FALSE)
                pass
            elif token in [33]:
                self.state = 145
                self.match(EsperadosParser.NAME)
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
        self.enterRule(localctx, 30, self.RULE_printExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(EsperadosParser.PRINT)
            self.state = 149
            self.match(EsperadosParser.LP)
            self.state = 150
            self.expr()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 151
                self.match(EsperadosParser.COMMA)
                self.state = 152
                self.expr()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
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
        self.enterRule(localctx, 32, self.RULE_variableExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(EsperadosParser.VARDEF)
            self.state = 161
            self.match(EsperadosParser.NAME)
            self.state = 162
            self.match(EsperadosParser.ASS)
            self.state = 163
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






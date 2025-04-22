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
        4,1,39,195,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,
        1,2,5,2,57,8,2,10,2,12,2,60,9,2,1,2,1,2,1,3,1,3,1,3,5,3,67,8,3,10,
        3,12,3,70,9,3,1,3,3,3,73,8,3,1,4,1,4,1,4,3,4,78,8,4,1,5,1,5,1,5,
        1,5,1,5,5,5,85,8,5,10,5,12,5,88,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,5,7,99,8,7,10,7,12,7,102,9,7,1,7,3,7,105,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,133,8,12,10,12,12,12,
        136,9,12,1,13,1,13,1,13,5,13,141,8,13,10,13,12,13,144,9,13,1,14,
        1,14,1,14,3,14,149,8,14,1,15,1,15,1,15,5,15,154,8,15,10,15,12,15,
        157,9,15,1,16,1,16,1,16,5,16,162,8,16,10,16,12,16,165,9,16,1,17,
        1,17,1,17,5,17,170,8,17,10,17,12,17,173,9,17,1,18,1,18,1,18,5,18,
        178,8,18,10,18,12,18,181,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,3,19,193,8,19,1,19,0,0,20,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,0,4,1,0,36,37,1,0,23,28,1,0,9,10,1,
        0,11,13,200,0,44,1,0,0,0,2,51,1,0,0,0,4,53,1,0,0,0,6,68,1,0,0,0,
        8,77,1,0,0,0,10,79,1,0,0,0,12,91,1,0,0,0,14,96,1,0,0,0,16,106,1,
        0,0,0,18,114,1,0,0,0,20,122,1,0,0,0,22,127,1,0,0,0,24,129,1,0,0,
        0,26,137,1,0,0,0,28,148,1,0,0,0,30,150,1,0,0,0,32,158,1,0,0,0,34,
        166,1,0,0,0,36,174,1,0,0,0,38,192,1,0,0,0,40,43,3,2,1,0,41,43,5,
        39,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,
        45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,5,1,0,0,48,49,3,6,3,
        0,49,50,5,0,0,1,50,1,1,0,0,0,51,52,7,0,0,0,52,3,1,0,0,0,53,58,5,
        2,0,0,54,57,3,2,1,0,55,57,5,39,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,
        60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,
        0,61,62,5,0,0,1,62,5,1,0,0,0,63,67,3,2,1,0,64,67,3,8,4,0,65,67,5,
        39,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,
        66,1,0,0,0,68,69,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,71,73,3,4,2,
        0,72,71,1,0,0,0,72,73,1,0,0,0,73,7,1,0,0,0,74,78,3,10,5,0,75,78,
        3,12,6,0,76,78,3,14,7,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,
        0,78,9,1,0,0,0,79,80,5,3,0,0,80,81,5,15,0,0,81,86,3,22,11,0,82,83,
        5,19,0,0,83,85,3,22,11,0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,
        0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,90,5,16,0,0,90,11,
        1,0,0,0,91,92,5,4,0,0,92,93,5,35,0,0,93,94,5,8,0,0,94,95,3,22,11,
        0,95,13,1,0,0,0,96,100,3,16,8,0,97,99,3,18,9,0,98,97,1,0,0,0,99,
        102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,104,1,0,0,0,102,100,
        1,0,0,0,103,105,3,20,10,0,104,103,1,0,0,0,104,105,1,0,0,0,105,15,
        1,0,0,0,106,107,5,5,0,0,107,108,5,15,0,0,108,109,3,22,11,0,109,110,
        5,16,0,0,110,111,5,17,0,0,111,112,3,6,3,0,112,113,5,18,0,0,113,17,
        1,0,0,0,114,115,5,7,0,0,115,116,5,15,0,0,116,117,3,22,11,0,117,118,
        5,16,0,0,118,119,5,17,0,0,119,120,3,6,3,0,120,121,5,18,0,0,121,19,
        1,0,0,0,122,123,5,6,0,0,123,124,5,17,0,0,124,125,3,6,3,0,125,126,
        5,18,0,0,126,21,1,0,0,0,127,128,3,24,12,0,128,23,1,0,0,0,129,134,
        3,26,13,0,130,131,5,30,0,0,131,133,3,26,13,0,132,130,1,0,0,0,133,
        136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,25,1,0,0,0,136,134,
        1,0,0,0,137,142,3,28,14,0,138,139,5,29,0,0,139,141,3,28,14,0,140,
        138,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,
        27,1,0,0,0,144,142,1,0,0,0,145,146,5,31,0,0,146,149,3,28,14,0,147,
        149,3,30,15,0,148,145,1,0,0,0,148,147,1,0,0,0,149,29,1,0,0,0,150,
        155,3,32,16,0,151,152,7,1,0,0,152,154,3,32,16,0,153,151,1,0,0,0,
        154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,31,1,0,0,0,157,
        155,1,0,0,0,158,163,3,34,17,0,159,160,7,2,0,0,160,162,3,34,17,0,
        161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,
        164,33,1,0,0,0,165,163,1,0,0,0,166,171,3,36,18,0,167,168,7,3,0,0,
        168,170,3,36,18,0,169,167,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,
        0,171,172,1,0,0,0,172,35,1,0,0,0,173,171,1,0,0,0,174,179,3,38,19,
        0,175,176,5,14,0,0,176,178,3,38,19,0,177,175,1,0,0,0,178,181,1,0,
        0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,37,1,0,0,0,181,179,1,0,0,
        0,182,183,5,15,0,0,183,184,3,22,11,0,184,185,5,16,0,0,185,193,1,
        0,0,0,186,193,5,32,0,0,187,193,5,34,0,0,188,193,5,33,0,0,189,193,
        5,21,0,0,190,193,5,22,0,0,191,193,5,35,0,0,192,182,1,0,0,0,192,186,
        1,0,0,0,192,187,1,0,0,0,192,188,1,0,0,0,192,189,1,0,0,0,192,190,
        1,0,0,0,192,191,1,0,0,0,193,39,1,0,0,0,19,42,44,56,58,66,68,72,77,
        86,100,104,134,142,148,155,163,171,179,192
    ]

class EsperadosParser ( Parser ):

    grammarFileName = "Esperados.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Saluton'", "'Adiau'", "'skribi'", "'variablo'", 
                     "'se'", "'alie'", "'alie se'", "'asigini'", "'aldoni'", 
                     "'subtrahi'", "'multigi'", "'dividi'", "'modulo'", 
                     "'intensigi'", "'('", "')'", "'{'", "'}'", "','", "'.'", 
                     "'vere'", "'malvero'", "'egala'", "'ne egala'", "'granda'", 
                     "'malgranda'", "'granda egala'", "'malgranda egala'", 
                     "'kaj'", "'au'", "'ne'" ]

    symbolicNames = [ "<INVALID>", "GREETING", "GOODBYE", "PRINT", "VARDEF", 
                      "IF", "ELSE", "ELIF", "ASS", "ADD", "SUB", "MULT", 
                      "DIV", "MOD", "EXPON", "LP", "RP", "LC", "RC", "COMMA", 
                      "DOT", "TRUE", "FALSE", "EQUAL", "INEQUAL", "GREATER", 
                      "LESS", "EGREATER", "ELESS", "AND", "OR", "NOT", "INT", 
                      "STRING", "FLOAT", "NAME", "COMMENT", "COMMENTBLOCK", 
                      "WS", "NL" ]

    RULE_program = 0
    RULE_comment = 1
    RULE_goodbye = 2
    RULE_instructions = 3
    RULE_action = 4
    RULE_printExpr = 5
    RULE_variableExpr = 6
    RULE_condition = 7
    RULE_ifExpr = 8
    RULE_elifExpr = 9
    RULE_elseExpr = 10
    RULE_expr = 11
    RULE_orExpr = 12
    RULE_andExpr = 13
    RULE_notExpr = 14
    RULE_comparisonExpr = 15
    RULE_additionExpr = 16
    RULE_multiExpr = 17
    RULE_exponExpr = 18
    RULE_atom = 19

    ruleNames =  [ "program", "comment", "goodbye", "instructions", "action", 
                   "printExpr", "variableExpr", "condition", "ifExpr", "elifExpr", 
                   "elseExpr", "expr", "orExpr", "andExpr", "notExpr", "comparisonExpr", 
                   "additionExpr", "multiExpr", "exponExpr", "atom" ]

    EOF = Token.EOF
    GREETING=1
    GOODBYE=2
    PRINT=3
    VARDEF=4
    IF=5
    ELSE=6
    ELIF=7
    ASS=8
    ADD=9
    SUB=10
    MULT=11
    DIV=12
    MOD=13
    EXPON=14
    LP=15
    RP=16
    LC=17
    RC=18
    COMMA=19
    DOT=20
    TRUE=21
    FALSE=22
    EQUAL=23
    INEQUAL=24
    GREATER=25
    LESS=26
    EGREATER=27
    ELESS=28
    AND=29
    OR=30
    NOT=31
    INT=32
    STRING=33
    FLOAT=34
    NAME=35
    COMMENT=36
    COMMENTBLOCK=37
    WS=38
    NL=39

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
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 755914244096) != 0):
                self.state = 42
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [36, 37]:
                    self.state = 40
                    self.comment()
                    pass
                elif token in [39]:
                    self.state = 41
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(EsperadosParser.GREETING)
            self.state = 48
            self.instructions()
            self.state = 49
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
            self.state = 51
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
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
        self.enterRule(localctx, 4, self.RULE_goodbye)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(EsperadosParser.GOODBYE)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 755914244096) != 0):
                self.state = 56
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [36, 37]:
                    self.state = 54
                    self.comment()
                    pass
                elif token in [39]:
                    self.state = 55
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(EsperadosParser.EOF)
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
        self.enterRule(localctx, 6, self.RULE_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 755914244152) != 0):
                self.state = 66
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [36, 37]:
                    self.state = 63
                    self.comment()
                    pass
                elif token in [3, 4, 5]:
                    self.state = 64
                    self.action()
                    pass
                elif token in [39]:
                    self.state = 65
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 71
                self.goodbye()


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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.printExpr()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.variableExpr()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
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
        self.enterRule(localctx, 10, self.RULE_printExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(EsperadosParser.PRINT)
            self.state = 80
            self.match(EsperadosParser.LP)
            self.state = 81
            self.expr()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 82
                self.match(EsperadosParser.COMMA)
                self.state = 83
                self.expr()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
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
        self.enterRule(localctx, 12, self.RULE_variableExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(EsperadosParser.VARDEF)
            self.state = 92
            self.match(EsperadosParser.NAME)
            self.state = 93
            self.match(EsperadosParser.ASS)
            self.state = 94
            self.expr()
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

        def ifExpr(self):
            return self.getTypedRuleContext(EsperadosParser.IfExprContext,0)


        def elifExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.ElifExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.ElifExprContext,i)


        def elseExpr(self):
            return self.getTypedRuleContext(EsperadosParser.ElseExprContext,0)


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
        self.enterRule(localctx, 14, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.ifExpr()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 97
                self.elifExpr()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 103
                self.elseExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExprContext(ParserRuleContext):
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
            return EsperadosParser.RULE_ifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfExpr" ):
                listener.enterIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfExpr" ):
                listener.exitIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExpr" ):
                return visitor.visitIfExpr(self)
            else:
                return visitor.visitChildren(self)




    def ifExpr(self):

        localctx = EsperadosParser.IfExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(EsperadosParser.IF)
            self.state = 107
            self.match(EsperadosParser.LP)
            self.state = 108
            self.expr()
            self.state = 109
            self.match(EsperadosParser.RP)
            self.state = 110
            self.match(EsperadosParser.LC)
            self.state = 111
            self.instructions()
            self.state = 112
            self.match(EsperadosParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(EsperadosParser.ELIF, 0)

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
            return EsperadosParser.RULE_elifExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifExpr" ):
                listener.enterElifExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifExpr" ):
                listener.exitElifExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifExpr" ):
                return visitor.visitElifExpr(self)
            else:
                return visitor.visitChildren(self)




    def elifExpr(self):

        localctx = EsperadosParser.ElifExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elifExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(EsperadosParser.ELIF)
            self.state = 115
            self.match(EsperadosParser.LP)
            self.state = 116
            self.expr()
            self.state = 117
            self.match(EsperadosParser.RP)
            self.state = 118
            self.match(EsperadosParser.LC)
            self.state = 119
            self.instructions()
            self.state = 120
            self.match(EsperadosParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(EsperadosParser.ELSE, 0)

        def LC(self):
            return self.getToken(EsperadosParser.LC, 0)

        def instructions(self):
            return self.getTypedRuleContext(EsperadosParser.InstructionsContext,0)


        def RC(self):
            return self.getToken(EsperadosParser.RC, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_elseExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseExpr" ):
                listener.enterElseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseExpr" ):
                listener.exitElseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseExpr" ):
                return visitor.visitElseExpr(self)
            else:
                return visitor.visitChildren(self)




    def elseExpr(self):

        localctx = EsperadosParser.ElseExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elseExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(EsperadosParser.ELSE)
            self.state = 123
            self.match(EsperadosParser.LC)
            self.state = 124
            self.instructions()
            self.state = 125
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
        self.enterRule(localctx, 22, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
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
        self.enterRule(localctx, 24, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.andExpr()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 130
                self.match(EsperadosParser.OR)
                self.state = 131
                self.andExpr()
                self.state = 136
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
        self.enterRule(localctx, 26, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.notExpr()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 138
                self.match(EsperadosParser.AND)
                self.state = 139
                self.notExpr()
                self.state = 144
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
        self.enterRule(localctx, 28, self.RULE_notExpr)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(EsperadosParser.NOT)
                self.state = 146
                self.notExpr()
                pass
            elif token in [15, 21, 22, 32, 33, 34, 35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
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
        self.enterRule(localctx, 30, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.additionExpr()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0):
                self.state = 151
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                self.additionExpr()
                self.state = 157
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

        def multiExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.MultiExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.MultiExprContext,i)


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
        self.enterRule(localctx, 32, self.RULE_additionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.multiExpr()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 159
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 160
                self.multiExpr()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.ExponExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.ExponExprContext,i)


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
            return EsperadosParser.RULE_multiExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiExpr" ):
                listener.enterMultiExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiExpr" ):
                listener.exitMultiExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiExpr" ):
                return visitor.visitMultiExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiExpr(self):

        localctx = EsperadosParser.MultiExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.exponExpr()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0):
                self.state = 167
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168
                self.exponExpr()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponExprContext(ParserRuleContext):
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
            return EsperadosParser.RULE_exponExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponExpr" ):
                listener.enterExponExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponExpr" ):
                listener.exitExponExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponExpr" ):
                return visitor.visitExponExpr(self)
            else:
                return visitor.visitChildren(self)




    def exponExpr(self):

        localctx = EsperadosParser.ExponExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exponExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.atom()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 175
                self.match(EsperadosParser.EXPON)
                self.state = 176
                self.atom()
                self.state = 181
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
        self.enterRule(localctx, 38, self.RULE_atom)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(EsperadosParser.LP)
                self.state = 183
                self.expr()
                self.state = 184
                self.match(EsperadosParser.RP)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(EsperadosParser.INT)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(EsperadosParser.FLOAT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                self.match(EsperadosParser.STRING)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.match(EsperadosParser.TRUE)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.match(EsperadosParser.FALSE)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 7)
                self.state = 191
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






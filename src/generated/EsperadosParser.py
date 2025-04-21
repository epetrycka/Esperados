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
        4,1,31,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,5,0,25,8,0,10,0,12,0,
        28,9,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,2,
        42,9,2,1,2,3,2,45,8,2,1,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,3,1,
        3,1,3,1,4,1,4,3,4,59,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,85,8,
        8,1,9,1,9,1,9,1,9,3,9,91,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,
        10,100,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,4,1,0,28,29,
        2,0,24,24,26,27,1,0,6,11,1,0,16,21,106,0,26,1,0,0,0,2,32,1,0,0,0,
        4,34,1,0,0,0,6,46,1,0,0,0,8,58,1,0,0,0,10,60,1,0,0,0,12,66,1,0,0,
        0,14,72,1,0,0,0,16,84,1,0,0,0,18,86,1,0,0,0,20,94,1,0,0,0,22,25,
        3,2,1,0,23,25,5,31,0,0,24,22,1,0,0,0,24,23,1,0,0,0,25,28,1,0,0,0,
        26,24,1,0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,29,30,3,
        4,2,0,30,31,5,0,0,1,31,1,1,0,0,0,32,33,7,0,0,0,33,3,1,0,0,0,34,40,
        5,1,0,0,35,39,3,2,1,0,36,39,3,8,4,0,37,39,5,31,0,0,38,35,1,0,0,0,
        38,36,1,0,0,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,
        0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,43,45,3,6,3,0,44,43,1,0,0,0,44,
        45,1,0,0,0,45,5,1,0,0,0,46,51,5,2,0,0,47,50,3,2,1,0,48,50,5,31,0,
        0,49,47,1,0,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,7,1,0,0,0,56,
        59,3,18,9,0,57,59,3,20,10,0,58,56,1,0,0,0,58,57,1,0,0,0,59,9,1,0,
        0,0,60,61,5,12,0,0,61,62,7,1,0,0,62,63,7,2,0,0,63,64,7,1,0,0,64,
        65,5,13,0,0,65,11,1,0,0,0,66,67,5,12,0,0,67,68,5,25,0,0,68,69,5,
        6,0,0,69,70,5,25,0,0,70,71,5,13,0,0,71,13,1,0,0,0,72,73,5,12,0,0,
        73,74,3,16,8,0,74,75,7,3,0,0,75,76,3,16,8,0,76,77,5,13,0,0,77,15,
        1,0,0,0,78,85,5,25,0,0,79,85,5,24,0,0,80,85,5,26,0,0,81,85,3,10,
        5,0,82,85,5,27,0,0,83,85,3,12,6,0,84,78,1,0,0,0,84,79,1,0,0,0,84,
        80,1,0,0,0,84,81,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,17,1,0,0,
        0,86,87,5,3,0,0,87,90,5,12,0,0,88,91,3,16,8,0,89,91,3,14,7,0,90,
        88,1,0,0,0,90,89,1,0,0,0,91,92,1,0,0,0,92,93,5,13,0,0,93,19,1,0,
        0,0,94,95,5,4,0,0,95,96,5,27,0,0,96,99,5,5,0,0,97,100,3,16,8,0,98,
        100,3,14,7,0,99,97,1,0,0,0,99,98,1,0,0,0,100,21,1,0,0,0,11,24,26,
        38,40,44,49,51,58,84,90,99
    ]

class EsperadosParser ( Parser ):

    grammarFileName = "Esperados.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Saluton'", "'Adiau'", "'skribi'", "'variablo'", 
                     "'asigini'", "'aldoni'", "'subtrahi'", "'multigi'", 
                     "'dividi'", "'modulo'", "'intensigi'", "'('", "')'", 
                     "'vere'", "'malvero'", "'egala'", "'ne egala'", "'granda'", 
                     "'malgranda'", "'granda egala'", "'malgranda egala'", 
                     "'kaj'", "'au'" ]

    symbolicNames = [ "<INVALID>", "GREETING", "GOODBYE", "PRINT", "VARDEF", 
                      "ASS", "ADD", "SUB", "MULT", "DIV", "MOD", "EXPON", 
                      "LP", "RP", "TRUE", "FALSE", "EQUAL", "INEQUAL", "GREATER", 
                      "LESS", "EGREATER", "ELESS", "AND", "OR", "INT", "STRING", 
                      "FLOAT", "NAME", "COMMENT", "COMMENTBLOCK", "WS", 
                      "NL" ]

    RULE_program = 0
    RULE_comment = 1
    RULE_greeting = 2
    RULE_goodbye = 3
    RULE_action = 4
    RULE_algebraExpr = 5
    RULE_addStrings = 6
    RULE_boolExpr = 7
    RULE_expr = 8
    RULE_printExpr = 9
    RULE_variableExpr = 10

    ruleNames =  [ "program", "comment", "greeting", "goodbye", "action", 
                   "algebraExpr", "addStrings", "boolExpr", "expr", "printExpr", 
                   "variableExpr" ]

    EOF = Token.EOF
    GREETING=1
    GOODBYE=2
    PRINT=3
    VARDEF=4
    ASS=5
    ADD=6
    SUB=7
    MULT=8
    DIV=9
    MOD=10
    EXPON=11
    LP=12
    RP=13
    TRUE=14
    FALSE=15
    EQUAL=16
    INEQUAL=17
    GREATER=18
    LESS=19
    EGREATER=20
    ELESS=21
    AND=22
    OR=23
    INT=24
    STRING=25
    FLOAT=26
    NAME=27
    COMMENT=28
    COMMENTBLOCK=29
    WS=30
    NL=31

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

        def greeting(self):
            return self.getTypedRuleContext(EsperadosParser.GreetingContext,0)


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
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0):
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28, 29]:
                    self.state = 22
                    self.comment()
                    pass
                elif token in [31]:
                    self.state = 23
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.greeting()
            self.state = 30
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
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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


    class GreetingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREETING(self):
            return self.getToken(EsperadosParser.GREETING, 0)

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
            return EsperadosParser.RULE_greeting

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreeting" ):
                listener.enterGreeting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreeting" ):
                listener.exitGreeting(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreeting" ):
                return visitor.visitGreeting(self)
            else:
                return visitor.visitChildren(self)




    def greeting(self):

        localctx = EsperadosParser.GreetingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_greeting)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(EsperadosParser.GREETING)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790040) != 0):
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28, 29]:
                    self.state = 35
                    self.comment()
                    pass
                elif token in [3, 4]:
                    self.state = 36
                    self.action()
                    pass
                elif token in [31]:
                    self.state = 37
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 43
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
            self.state = 46
            self.match(EsperadosParser.GOODBYE)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2952790016) != 0):
                self.state = 49
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [28, 29]:
                    self.state = 47
                    self.comment()
                    pass
                elif token in [31]:
                    self.state = 48
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.printExpr()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.variableExpr()
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


    class AlgebraExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(EsperadosParser.LP, 0)

        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.INT)
            else:
                return self.getToken(EsperadosParser.INT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.FLOAT)
            else:
                return self.getToken(EsperadosParser.FLOAT, i)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.NAME)
            else:
                return self.getToken(EsperadosParser.NAME, i)

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
        self.enterRule(localctx, 10, self.RULE_algebraExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(EsperadosParser.LP)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 218103808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 218103808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64
            self.match(EsperadosParser.RP)
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

        def LP(self):
            return self.getToken(EsperadosParser.LP, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.STRING)
            else:
                return self.getToken(EsperadosParser.STRING, i)

        def ADD(self):
            return self.getToken(EsperadosParser.ADD, 0)

        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

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
        self.enterRule(localctx, 12, self.RULE_addStrings)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(EsperadosParser.LP)
            self.state = 67
            self.match(EsperadosParser.STRING)
            self.state = 68
            self.match(EsperadosParser.ADD)
            self.state = 69
            self.match(EsperadosParser.STRING)
            self.state = 70
            self.match(EsperadosParser.RP)
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

        def LP(self):
            return self.getToken(EsperadosParser.LP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperadosParser.ExprContext)
            else:
                return self.getTypedRuleContext(EsperadosParser.ExprContext,i)


        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

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
            self.state = 72
            self.match(EsperadosParser.LP)
            self.state = 73
            self.expr()
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 75
            self.expr()
            self.state = 76
            self.match(EsperadosParser.RP)
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

        def STRING(self):
            return self.getToken(EsperadosParser.STRING, 0)

        def INT(self):
            return self.getToken(EsperadosParser.INT, 0)

        def FLOAT(self):
            return self.getToken(EsperadosParser.FLOAT, 0)

        def algebraExpr(self):
            return self.getTypedRuleContext(EsperadosParser.AlgebraExprContext,0)


        def NAME(self):
            return self.getToken(EsperadosParser.NAME, 0)

        def addStrings(self):
            return self.getTypedRuleContext(EsperadosParser.AddStringsContext,0)


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
        self.enterRule(localctx, 16, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 78
                self.match(EsperadosParser.STRING)
                pass

            elif la_ == 2:
                self.state = 79
                self.match(EsperadosParser.INT)
                pass

            elif la_ == 3:
                self.state = 80
                self.match(EsperadosParser.FLOAT)
                pass

            elif la_ == 4:
                self.state = 81
                self.algebraExpr()
                pass

            elif la_ == 5:
                self.state = 82
                self.match(EsperadosParser.NAME)
                pass

            elif la_ == 6:
                self.state = 83
                self.addStrings()
                pass


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

        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


        def boolExpr(self):
            return self.getTypedRuleContext(EsperadosParser.BoolExprContext,0)


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
        self.enterRule(localctx, 18, self.RULE_printExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(EsperadosParser.PRINT)
            self.state = 87
            self.match(EsperadosParser.LP)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 88
                self.expr()
                pass

            elif la_ == 2:
                self.state = 89
                self.boolExpr()
                pass


            self.state = 92
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


        def boolExpr(self):
            return self.getTypedRuleContext(EsperadosParser.BoolExprContext,0)


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
        self.enterRule(localctx, 20, self.RULE_variableExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(EsperadosParser.VARDEF)
            self.state = 95
            self.match(EsperadosParser.NAME)
            self.state = 96
            self.match(EsperadosParser.ASS)
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 97
                self.expr()
                pass

            elif la_ == 2:
                self.state = 98
                self.boolExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






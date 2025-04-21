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
        4,1,9,28,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        0,0,4,0,2,4,6,0,1,1,0,6,7,25,0,8,1,0,0,0,2,18,1,0,0,0,4,20,1,0,0,
        0,6,22,1,0,0,0,8,11,5,3,0,0,9,12,3,2,1,0,10,12,5,9,0,0,11,9,1,0,
        0,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,
        1,0,0,0,15,16,5,4,0,0,16,17,5,0,0,1,17,1,1,0,0,0,18,19,3,6,3,0,19,
        3,1,0,0,0,20,21,7,0,0,0,21,5,1,0,0,0,22,23,5,5,0,0,23,24,5,1,0,0,
        24,25,3,4,2,0,25,26,5,2,0,0,26,7,1,0,0,0,2,11,13
    ]

class EsperadosParser ( Parser ):

    grammarFileName = "Esperados.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'Saluton'", "'Adiau'", 
                     "'skribi'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "GREETING", 
                      "GOODBYE", "PRINT", "INT", "STRING", "WS", "NL" ]

    RULE_program = 0
    RULE_action = 1
    RULE_expr = 2
    RULE_printExpr = 3

    ruleNames =  [ "program", "action", "expr", "printExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    GREETING=3
    GOODBYE=4
    PRINT=5
    INT=6
    STRING=7
    WS=8
    NL=9

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

        def GOODBYE(self):
            return self.getToken(EsperadosParser.GOODBYE, 0)

        def EOF(self):
            return self.getToken(EsperadosParser.EOF, 0)

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
            self.state = 8
            self.match(EsperadosParser.GREETING)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 9
                    self.action()
                    pass
                elif token in [9]:
                    self.state = 10
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==9):
                    break

            self.state = 15
            self.match(EsperadosParser.GOODBYE)
            self.state = 16
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
        self.enterRule(localctx, 2, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.printExpr()
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
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
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


    class PrintExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(EsperadosParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


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
        self.enterRule(localctx, 6, self.RULE_printExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(EsperadosParser.PRINT)
            self.state = 23
            self.match(EsperadosParser.T__0)
            self.state = 24
            self.expr()
            self.state = 25
            self.match(EsperadosParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






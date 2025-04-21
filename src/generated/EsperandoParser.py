# Generated from Esperando.g4 by ANTLR 4.13.2
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
        4,1,7,30,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,3,1,19,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,27,0,11,1,0,0,0,2,18,1,0,0,0,4,20,
        1,0,0,0,6,22,1,0,0,0,8,24,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,
        13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,19,3,4,2,
        0,16,19,3,8,4,0,17,19,3,6,3,0,18,15,1,0,0,0,18,16,1,0,0,0,18,17,
        1,0,0,0,19,3,1,0,0,0,20,21,5,1,0,0,21,5,1,0,0,0,22,23,5,2,0,0,23,
        7,1,0,0,0,24,25,5,3,0,0,25,26,5,4,0,0,26,27,5,6,0,0,27,28,5,5,0,
        0,28,9,1,0,0,0,2,13,18
    ]

class EsperandoParser ( Parser ):

    grammarFileName = "Esperando.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Saluton'", "'Adiau'", "'skribi'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_greeting = 2
    RULE_goodbye = 3
    RULE_printStmt = 4

    ruleNames =  [ "program", "statement", "greeting", "goodbye", "printStmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    STRING=6
    WS=7

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EsperandoParser.StatementContext)
            else:
                return self.getTypedRuleContext(EsperandoParser.StatementContext,i)


        def getRuleIndex(self):
            return EsperandoParser.RULE_program

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

        localctx = EsperandoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def greeting(self):
            return self.getTypedRuleContext(EsperandoParser.GreetingContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(EsperandoParser.PrintStmtContext,0)


        def goodbye(self):
            return self.getTypedRuleContext(EsperandoParser.GoodbyeContext,0)


        def getRuleIndex(self):
            return EsperandoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = EsperandoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.greeting()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.printStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                self.goodbye()
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


    class GreetingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return EsperandoParser.RULE_greeting

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

        localctx = EsperandoParser.GreetingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_greeting)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(EsperandoParser.T__0)
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


        def getRuleIndex(self):
            return EsperandoParser.RULE_goodbye

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

        localctx = EsperandoParser.GoodbyeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_goodbye)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(EsperandoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(EsperandoParser.STRING, 0)

        def getRuleIndex(self):
            return EsperandoParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = EsperandoParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(EsperandoParser.T__2)
            self.state = 25
            self.match(EsperandoParser.T__3)
            self.state = 26
            self.match(EsperandoParser.STRING)
            self.state = 27
            self.match(EsperandoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






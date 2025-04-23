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
        4,1,48,237,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,1,0,5,0,49,8,0,10,0,12,0,52,9,0,1,0,
        1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,
        1,2,1,3,1,3,1,3,5,3,73,8,3,10,3,12,3,76,9,3,1,3,3,3,79,8,3,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,88,8,4,1,5,1,5,1,5,1,5,1,5,5,5,95,8,5,
        10,5,12,5,98,9,5,1,5,1,5,1,6,3,6,103,8,6,1,6,1,6,1,6,3,6,108,8,6,
        1,6,1,6,1,6,1,7,1,7,5,7,115,8,7,10,7,12,7,118,9,7,1,7,3,7,121,8,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,153,8,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,5,14,173,8,14,10,
        14,12,14,176,9,14,1,15,1,15,1,15,5,15,181,8,15,10,15,12,15,184,9,
        15,1,16,1,16,1,16,3,16,189,8,16,1,17,1,17,1,17,5,17,194,8,17,10,
        17,12,17,197,9,17,1,18,1,18,1,18,5,18,202,8,18,10,18,12,18,205,9,
        18,1,19,1,19,1,19,5,19,210,8,19,10,19,12,19,213,9,19,1,20,1,20,1,
        20,5,20,218,8,20,10,20,12,20,221,9,20,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,3,21,233,8,21,1,22,1,22,1,22,0,0,23,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,5,1,
        0,45,46,1,0,28,33,1,0,11,12,1,0,13,15,1,0,38,40,246,0,50,1,0,0,0,
        2,57,1,0,0,0,4,59,1,0,0,0,6,74,1,0,0,0,8,87,1,0,0,0,10,89,1,0,0,
        0,12,102,1,0,0,0,14,112,1,0,0,0,16,122,1,0,0,0,18,130,1,0,0,0,20,
        138,1,0,0,0,22,143,1,0,0,0,24,159,1,0,0,0,26,167,1,0,0,0,28,169,
        1,0,0,0,30,177,1,0,0,0,32,188,1,0,0,0,34,190,1,0,0,0,36,198,1,0,
        0,0,38,206,1,0,0,0,40,214,1,0,0,0,42,232,1,0,0,0,44,234,1,0,0,0,
        46,49,3,2,1,0,47,49,5,48,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,52,1,
        0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,
        54,5,1,0,0,54,55,3,6,3,0,55,56,5,0,0,1,56,1,1,0,0,0,57,58,7,0,0,
        0,58,3,1,0,0,0,59,64,5,2,0,0,60,63,3,2,1,0,61,63,5,48,0,0,62,60,
        1,0,0,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,
        65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,0,0,1,68,5,1,0,0,0,69,73,3,2,
        1,0,70,73,3,8,4,0,71,73,5,48,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,
        71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,78,1,0,0,
        0,76,74,1,0,0,0,77,79,3,4,2,0,78,77,1,0,0,0,78,79,1,0,0,0,79,7,1,
        0,0,0,80,88,3,10,5,0,81,88,3,12,6,0,82,88,3,14,7,0,83,88,3,22,11,
        0,84,88,3,24,12,0,85,88,5,26,0,0,86,88,5,27,0,0,87,80,1,0,0,0,87,
        81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,
        0,87,86,1,0,0,0,88,9,1,0,0,0,89,90,5,3,0,0,90,91,5,17,0,0,91,96,
        3,26,13,0,92,93,5,21,0,0,93,95,3,26,13,0,94,92,1,0,0,0,95,98,1,0,
        0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,99,100,
        5,18,0,0,100,11,1,0,0,0,101,103,5,37,0,0,102,101,1,0,0,0,102,103,
        1,0,0,0,103,104,1,0,0,0,104,105,5,4,0,0,105,107,5,44,0,0,106,108,
        3,44,22,0,107,106,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,110,
        5,10,0,0,110,111,3,26,13,0,111,13,1,0,0,0,112,116,3,16,8,0,113,115,
        3,18,9,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,
        1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,119,121,3,20,10,0,120,119,
        1,0,0,0,120,121,1,0,0,0,121,15,1,0,0,0,122,123,5,5,0,0,123,124,5,
        17,0,0,124,125,3,26,13,0,125,126,5,18,0,0,126,127,5,19,0,0,127,128,
        3,6,3,0,128,129,5,20,0,0,129,17,1,0,0,0,130,131,5,7,0,0,131,132,
        5,17,0,0,132,133,3,26,13,0,133,134,5,18,0,0,134,135,5,19,0,0,135,
        136,3,6,3,0,136,137,5,20,0,0,137,19,1,0,0,0,138,139,5,6,0,0,139,
        140,5,19,0,0,140,141,3,6,3,0,141,142,5,20,0,0,142,21,1,0,0,0,143,
        144,5,8,0,0,144,145,5,17,0,0,145,146,5,44,0,0,146,147,5,23,0,0,147,
        148,5,41,0,0,148,149,5,23,0,0,149,152,5,41,0,0,150,151,5,23,0,0,
        151,153,5,41,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,
        154,155,5,18,0,0,155,156,5,19,0,0,156,157,3,6,3,0,157,158,5,20,0,
        0,158,23,1,0,0,0,159,160,5,9,0,0,160,161,5,17,0,0,161,162,3,26,13,
        0,162,163,5,18,0,0,163,164,5,19,0,0,164,165,3,6,3,0,165,166,5,20,
        0,0,166,25,1,0,0,0,167,168,3,28,14,0,168,27,1,0,0,0,169,174,3,30,
        15,0,170,171,5,35,0,0,171,173,3,30,15,0,172,170,1,0,0,0,173,176,
        1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,29,1,0,0,0,176,174,1,
        0,0,0,177,182,3,32,16,0,178,179,5,34,0,0,179,181,3,32,16,0,180,178,
        1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,31,1,
        0,0,0,184,182,1,0,0,0,185,186,5,36,0,0,186,189,3,32,16,0,187,189,
        3,34,17,0,188,185,1,0,0,0,188,187,1,0,0,0,189,33,1,0,0,0,190,195,
        3,36,18,0,191,192,7,1,0,0,192,194,3,36,18,0,193,191,1,0,0,0,194,
        197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,35,1,0,0,0,197,195,
        1,0,0,0,198,203,3,38,19,0,199,200,7,2,0,0,200,202,3,38,19,0,201,
        199,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,
        37,1,0,0,0,205,203,1,0,0,0,206,211,3,40,20,0,207,208,7,3,0,0,208,
        210,3,40,20,0,209,207,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,
        212,1,0,0,0,212,39,1,0,0,0,213,211,1,0,0,0,214,219,3,42,21,0,215,
        216,5,16,0,0,216,218,3,42,21,0,217,215,1,0,0,0,218,221,1,0,0,0,219,
        217,1,0,0,0,219,220,1,0,0,0,220,41,1,0,0,0,221,219,1,0,0,0,222,223,
        5,17,0,0,223,224,3,26,13,0,224,225,5,18,0,0,225,233,1,0,0,0,226,
        233,5,41,0,0,227,233,5,43,0,0,228,233,5,42,0,0,229,233,5,24,0,0,
        230,233,5,25,0,0,231,233,5,44,0,0,232,222,1,0,0,0,232,226,1,0,0,
        0,232,227,1,0,0,0,232,228,1,0,0,0,232,229,1,0,0,0,232,230,1,0,0,
        0,232,231,1,0,0,0,233,43,1,0,0,0,234,235,7,4,0,0,235,45,1,0,0,0,
        22,48,50,62,64,72,74,78,87,96,102,107,116,120,152,174,182,188,195,
        203,211,219,232
    ]

class EsperadosParser ( Parser ):

    grammarFileName = "Esperados.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Saluton'", "'Adiau'", "'skribi'", "'variablo'", 
                     "'se'", "'alie'", "'alie se'", "'por'", "'gis'", "'asigini'", 
                     "'aldoni'", "'subtrahi'", "'multigi'", "'dividi'", 
                     "'modulo'", "'intensigi'", "'('", "')'", "'{'", "'}'", 
                     "','", "'.'", "';'", "'vere'", "'malvero'", "'haltu'", 
                     "'daurigi'", "'egala'", "'ne egala'", "'granda'", "'malgranda'", 
                     "'granda egala'", "'malgranda egala'", "'kaj'", "'au'", 
                     "'ne'", "'tutmonda'", "'entjero'", "'flosi'", "'snuro'" ]

    symbolicNames = [ "<INVALID>", "GREETING", "GOODBYE", "PRINT", "VARDEF", 
                      "IF", "ELSE", "ELIF", "FOR", "WHILE", "ASG", "ADD", 
                      "SUB", "MULT", "DIV", "MOD", "EXPON", "LP", "RP", 
                      "LC", "RC", "COMMA", "DOT", "SEMICOLON", "TRUE", "FALSE", 
                      "BREAK", "CONTINUE", "EQUAL", "INEQUAL", "GREATER", 
                      "LESS", "EGREATER", "ELESS", "AND", "OR", "NOT", "GLOBAL", 
                      "INTTYPE", "FLOATTYPE", "STRINGTYPE", "INT", "STRING", 
                      "FLOAT", "NAME", "COMMENT", "COMMENTBLOCK", "WS", 
                      "NL" ]

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
    RULE_forLoop = 11
    RULE_whileLoop = 12
    RULE_expr = 13
    RULE_orExpr = 14
    RULE_andExpr = 15
    RULE_notExpr = 16
    RULE_comparisonExpr = 17
    RULE_additionExpr = 18
    RULE_multiExpr = 19
    RULE_exponExpr = 20
    RULE_atom = 21
    RULE_type = 22

    ruleNames =  [ "program", "comment", "goodbye", "instructions", "action", 
                   "printExpr", "variableExpr", "condition", "ifExpr", "elifExpr", 
                   "elseExpr", "forLoop", "whileLoop", "expr", "orExpr", 
                   "andExpr", "notExpr", "comparisonExpr", "additionExpr", 
                   "multiExpr", "exponExpr", "atom", "type" ]

    EOF = Token.EOF
    GREETING=1
    GOODBYE=2
    PRINT=3
    VARDEF=4
    IF=5
    ELSE=6
    ELIF=7
    FOR=8
    WHILE=9
    ASG=10
    ADD=11
    SUB=12
    MULT=13
    DIV=14
    MOD=15
    EXPON=16
    LP=17
    RP=18
    LC=19
    RC=20
    COMMA=21
    DOT=22
    SEMICOLON=23
    TRUE=24
    FALSE=25
    BREAK=26
    CONTINUE=27
    EQUAL=28
    INEQUAL=29
    GREATER=30
    LESS=31
    EGREATER=32
    ELESS=33
    AND=34
    OR=35
    NOT=36
    GLOBAL=37
    INTTYPE=38
    FLOATTYPE=39
    STRINGTYPE=40
    INT=41
    STRING=42
    FLOAT=43
    NAME=44
    COMMENT=45
    COMMENTBLOCK=46
    WS=47
    NL=48

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
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 387028092977152) != 0):
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45, 46]:
                    self.state = 46
                    self.comment()
                    pass
                elif token in [48]:
                    self.state = 47
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(EsperadosParser.GREETING)
            self.state = 54
            self.instructions()
            self.state = 55
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
            self.state = 57
            _la = self._input.LA(1)
            if not(_la==45 or _la==46):
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
            self.state = 59
            self.match(EsperadosParser.GOODBYE)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 387028092977152) != 0):
                self.state = 62
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45, 46]:
                    self.state = 60
                    self.comment()
                    pass
                elif token in [48]:
                    self.state = 61
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
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
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 387165733258040) != 0):
                self.state = 72
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [45, 46]:
                    self.state = 69
                    self.comment()
                    pass
                elif token in [3, 4, 5, 8, 9, 26, 27, 37]:
                    self.state = 70
                    self.action()
                    pass
                elif token in [48]:
                    self.state = 71
                    self.match(EsperadosParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 77
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


        def forLoop(self):
            return self.getTypedRuleContext(EsperadosParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(EsperadosParser.WhileLoopContext,0)


        def BREAK(self):
            return self.getToken(EsperadosParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(EsperadosParser.CONTINUE, 0)

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
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.printExpr()
                pass
            elif token in [4, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.variableExpr()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.condition()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.forLoop()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.whileLoop()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.match(EsperadosParser.BREAK)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 7)
                self.state = 86
                self.match(EsperadosParser.CONTINUE)
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
            self.state = 89
            self.match(EsperadosParser.PRINT)
            self.state = 90
            self.match(EsperadosParser.LP)
            self.state = 91
            self.expr()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 92
                self.match(EsperadosParser.COMMA)
                self.state = 93
                self.expr()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
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

        def ASG(self):
            return self.getToken(EsperadosParser.ASG, 0)

        def expr(self):
            return self.getTypedRuleContext(EsperadosParser.ExprContext,0)


        def GLOBAL(self):
            return self.getToken(EsperadosParser.GLOBAL, 0)

        def type_(self):
            return self.getTypedRuleContext(EsperadosParser.TypeContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 101
                self.match(EsperadosParser.GLOBAL)


            self.state = 104
            self.match(EsperadosParser.VARDEF)
            self.state = 105
            self.match(EsperadosParser.NAME)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0):
                self.state = 106
                self.type_()


            self.state = 109
            self.match(EsperadosParser.ASG)
            self.state = 110
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
            self.state = 112
            self.ifExpr()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 113
                self.elifExpr()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 119
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
            self.state = 122
            self.match(EsperadosParser.IF)
            self.state = 123
            self.match(EsperadosParser.LP)
            self.state = 124
            self.expr()
            self.state = 125
            self.match(EsperadosParser.RP)
            self.state = 126
            self.match(EsperadosParser.LC)
            self.state = 127
            self.instructions()
            self.state = 128
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
            self.state = 130
            self.match(EsperadosParser.ELIF)
            self.state = 131
            self.match(EsperadosParser.LP)
            self.state = 132
            self.expr()
            self.state = 133
            self.match(EsperadosParser.RP)
            self.state = 134
            self.match(EsperadosParser.LC)
            self.state = 135
            self.instructions()
            self.state = 136
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
            self.state = 138
            self.match(EsperadosParser.ELSE)
            self.state = 139
            self.match(EsperadosParser.LC)
            self.state = 140
            self.instructions()
            self.state = 141
            self.match(EsperadosParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(EsperadosParser.FOR, 0)

        def LP(self):
            return self.getToken(EsperadosParser.LP, 0)

        def NAME(self):
            return self.getToken(EsperadosParser.NAME, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.SEMICOLON)
            else:
                return self.getToken(EsperadosParser.SEMICOLON, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(EsperadosParser.INT)
            else:
                return self.getToken(EsperadosParser.INT, i)

        def RP(self):
            return self.getToken(EsperadosParser.RP, 0)

        def LC(self):
            return self.getToken(EsperadosParser.LC, 0)

        def instructions(self):
            return self.getTypedRuleContext(EsperadosParser.InstructionsContext,0)


        def RC(self):
            return self.getToken(EsperadosParser.RC, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = EsperadosParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(EsperadosParser.FOR)
            self.state = 144
            self.match(EsperadosParser.LP)
            self.state = 145
            self.match(EsperadosParser.NAME)
            self.state = 146
            self.match(EsperadosParser.SEMICOLON)
            self.state = 147
            self.match(EsperadosParser.INT)
            self.state = 148
            self.match(EsperadosParser.SEMICOLON)
            self.state = 149
            self.match(EsperadosParser.INT)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 150
                self.match(EsperadosParser.SEMICOLON)
                self.state = 151
                self.match(EsperadosParser.INT)


            self.state = 154
            self.match(EsperadosParser.RP)
            self.state = 155
            self.match(EsperadosParser.LC)
            self.state = 156
            self.instructions()
            self.state = 157
            self.match(EsperadosParser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(EsperadosParser.WHILE, 0)

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
            return EsperadosParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = EsperadosParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(EsperadosParser.WHILE)
            self.state = 160
            self.match(EsperadosParser.LP)
            self.state = 161
            self.expr()
            self.state = 162
            self.match(EsperadosParser.RP)
            self.state = 163
            self.match(EsperadosParser.LC)
            self.state = 164
            self.instructions()
            self.state = 165
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
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 28, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.andExpr()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 170
                self.match(EsperadosParser.OR)
                self.state = 171
                self.andExpr()
                self.state = 176
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
        self.enterRule(localctx, 30, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.notExpr()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 178
                self.match(EsperadosParser.AND)
                self.state = 179
                self.notExpr()
                self.state = 184
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
        self.enterRule(localctx, 32, self.RULE_notExpr)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(EsperadosParser.NOT)
                self.state = 186
                self.notExpr()
                pass
            elif token in [17, 24, 25, 41, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
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
        self.enterRule(localctx, 34, self.RULE_comparisonExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.additionExpr()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0):
                self.state = 191
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.additionExpr()
                self.state = 197
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
        self.enterRule(localctx, 36, self.RULE_additionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.multiExpr()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.multiExpr()
                self.state = 205
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
        self.enterRule(localctx, 38, self.RULE_multiExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.exponExpr()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0):
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.exponExpr()
                self.state = 213
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
        self.enterRule(localctx, 40, self.RULE_exponExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.atom()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 215
                self.match(EsperadosParser.EXPON)
                self.state = 216
                self.atom()
                self.state = 221
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
        self.enterRule(localctx, 42, self.RULE_atom)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(EsperadosParser.LP)
                self.state = 223
                self.expr()
                self.state = 224
                self.match(EsperadosParser.RP)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(EsperadosParser.INT)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(EsperadosParser.FLOAT)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.match(EsperadosParser.STRING)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.match(EsperadosParser.TRUE)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.match(EsperadosParser.FALSE)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 7)
                self.state = 231
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


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(EsperadosParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(EsperadosParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(EsperadosParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return EsperadosParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = EsperadosParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
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






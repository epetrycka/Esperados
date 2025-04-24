grammar Esperados;
import EsperadosTokens, EsperadosExpr, EsperadosTab;

// PARSER

program         : (comment | NL)* GREETING instructions EOF ;

comment         : COMMENTBLOCK | COMMENT ;

goodbye         : GOODBYE (comment | NL)* EOF ;

instructions    : (comment | action | NL)* goodbye? ;

action          : printExpr
                | inputExpr
                | variableExpr
                | defList
                | condition 
                | forLoop 
                | whileLoop
                | functionDef
                | functionCall
                | deleteStmt;

printExpr       : PRINT LP expr (COMMA expr)* RP ;

inputExpr       : VARDEF type? NAME ASG INPUT LP RP;

variableExpr    : GLOBAL? VARDEF NAME type? ASG expr ;

condition       : ifExpr elifExpr* elseExpr? ;

ifExpr          : IF LP expr RP LC instructions RC ;

elifExpr        : ELIF LP expr RP LC instructions RC ;

elseExpr        : ELSE LC instructions RC ;

loopAction      : action
                | BREAK
                | CONTINUE ;

loopInstructions: (comment | loopAction | NL)* ;

forLoop         : FOR LP NAME SEMICOLON INT SEMICOLON INT SEMICOLON INT? RP LC loopInstructions RC ;

whileLoop       : WHILE LP expr RP LC loopInstructions RC ;

funDefAction    : action
                | returnStmt ;

funDefInstructions: (comment | funDefAction | NL)* ;

functionDef     : DEF NAME LP parameters? RP LC funDefInstructions RC ;

parameters      : (type COLON)? NAME (COMMA (type? COLON)? NAME)* ;

functionCall    : FUN NAME LP (NAME EQUALSIGN expr (COMMA NAME EQUALSIGN expr)*)? RP ;

returnStmt      : RETURN expr? ;

deleteStmt      : DEL NAME ;
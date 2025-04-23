grammar Esperados;
import EsperadosTokens, EsperadosExpr;

// PARSER

program         : (comment | NL)* GREETING instructions EOF ;

comment         : COMMENTBLOCK | COMMENT ;

goodbye         : GOODBYE (comment | NL)* EOF ;

instructions    : (comment | action | NL)* goodbye? ;

action          : printExpr
                | variableExpr
                | condition 
                | forLoop 
                | whileLoop
                | forEachLoop
                | functionDef
                | functionCall
                | deleteStmt;

printExpr       : PRINT LP expr (COMMA expr)* RP ;

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

forEachLoop     : FOREACH NAME IN expr LC instructions RC ;

funDefAction    : action
                | returnStmt ;

funDefInstructions: (comment | funAction | NL)* ;

functionDef     : DEF NAME LP parameters? RP LC funDefInstructions RC ;

parameters      : type? NAME (COMMA type? NAME)* ;

functionCall    : NAME LP (expr (COMMA expr)*)? RP ;

returnStmt      : RETURN expr? ;

deleteStmt      : DEL NAME ;
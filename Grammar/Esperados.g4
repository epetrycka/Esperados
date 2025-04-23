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
                | BREAK
                | CONTINUE ;

printExpr       : PRINT LP expr (COMMA expr)* RP ;

variableExpr    : GLOBAL? VARDEF NAME type? ASG expr ;

condition       : ifExpr elifExpr* elseExpr? ;

ifExpr          : IF LP expr RP LC instructions RC ;

elifExpr        : ELIF LP expr RP LC instructions RC ;

elseExpr        : ELSE LC instructions RC ;

//pętla do iterowania po liczbach całkowity z opcją zdefiniowania różnicy (default: 1)
forLoop         : FOR LP NAME SEMICOLON INT SEMICOLON INT (SEMICOLON INT)? RP LC instructions RC ; 

whileLoop       : WHILE LP expr RP LC instructions RC ;
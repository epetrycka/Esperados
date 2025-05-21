grammar Esperados;
import EsperadosTokens, EsperadosExpr;

// PARSER

program         : skipBefore (GREETING instructions* GOODBYE skipAfter)? EOF ;

skipBefore      : (~(GREETING | GOODBYE))*;

skipAfter       : ( . )*? ;

instructions    : printExpr
                | variableExpr
                | deleteStmt
                | condition 
                | forLoop 
                | forEachLoop
                | whileLoop
                | functionDef
                | functionCall
                | defList
                | addToList
                | removeFromList
                | insertToList
                | returnStmt
                | replaceInStruct
                | defDict
                ;

actions         : instructions
                | BREAK
                | CONTINUE ;

printExpr       : PRINT LP expr (COMMA expr)* RP ;

variableExpr    : GLOBAL? VARDEF type? NAME ASG (expr | INPUT LP RP);

deleteStmt      : DEL NAME ;

condition       : ifExpr elifExpr* elseExpr? ;

ifExpr          : IF LP expr RP LC actions* RC ;

elifExpr        : ELIF LP expr RP LC actions* RC ;

elseExpr        : ELSE LC actions* RC ;

forLoop         : FOR LP NAME SEMICOLON INT SEMICOLON INT SEMICOLON INT? RP LC actions* RC ;

whileLoop       : WHILE LP expr RP LC actions* RC ;

forEachLoop     : FOREACH NAME IN NAME LC actions* RC ;

functionDef     : DEF NAME LP parameters? RP LC actions* RC ;

parameters      : (type COLON)? NAME (COMMA (type? COLON)? NAME)* ;

returnStmt      : RETURN expr? ;

defList         : GLOBAL? VARDEF LIST NAME ASG LS (expr (COMMA expr)*)? PS ;

addToList       : NAME ADD expr ;

removeFromList  : NAME SUB expr ;

insertToList    : NAME ADD LP expr COMMA expr RP ;

replaceInStruct : NAME LS expr PS ASG expr ;

defDict         : GLOBAL? VARDEF DICT NAME ASG LC (expr COLON expr (COMMA expr COLON expr)*)? RC ;
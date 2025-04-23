grammar Esperados;

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

expr            : orExpr ;

orExpr          : andExpr (OR andExpr)* ;

andExpr         : notExpr (AND notExpr)* ;

notExpr         : NOT notExpr
                | comparisonExpr ;

comparisonExpr  : additionExpr ((EQUAL | INEQUAL | GREATER | LESS | EGREATER | ELESS) additionExpr)* ;

additionExpr    : multiExpr ((ADD | SUB) multiExpr)* ;

multiExpr       : exponExpr ((MULT | DIV | MOD) exponExpr)* ;

exponExpr       : atom (EXPON atom)* ;

atom            : LP expr RP
                | INT
                | FLOAT
                | STRING
                | TRUE
                | FALSE
                | NAME ;

type            : INTTYPE
                | FLOATTYPE
                | STRINGTYPE ;

// LEXER

GREETING        : 'Saluton' ;
GOODBYE         : 'Adiau' ;
PRINT           : 'skribi' ;
VARDEF          : 'variablo' ;
IF              : 'se' ;
ELSE            : 'alie' ;
ELIF            : 'alie se' ;
FOR             : 'por' ;
WHILE           : 'gis' ;

ASG             : 'asigini' ;
ADD             : 'aldoni' ;
SUB             : 'subtrahi' ;
MULT            : 'multigi' ;
DIV             : 'dividi' ;
MOD             : 'modulo' ;
EXPON           : 'intensigi' ;

LP              : '(' ;
RP              : ')' ;
LC              : '{' ;
RC              : '}' ;
COMMA           : ',' ;
DOT             : '.' ;
SEMICOLON       : ';' ;

TRUE            : 'vere' ;
FALSE           : 'malvero' ;
BREAK           : 'haltu' ;
CONTINUE        : 'daurigi' ; 

EQUAL           : 'egala' ;
INEQUAL         : 'ne egala' ;
GREATER         : 'granda' ;
LESS            : 'malgranda' ;
EGREATER        : 'granda egala' ;
ELESS           : 'malgranda egala' ;

AND             : 'kaj' ;
OR              : 'au' ;
NOT             : 'ne' ;

GLOBAL          : 'tutmonda' ;
INTTYPE         : 'entjero' ;
FLOATTYPE       : 'flosi' ;
STRINGTYPE      : 'snuro' ;    

INT             : [0-9]+ ;
fragment ESC    : '\\' ["\\/bfnrt] ;
STRING          : '"' (ESC | ~["\\\r\n])* '"' ;
FLOAT           : [0-9]+ '.' [0-9]+ ;

NAME            : [a-zA-Z] [a-zA-Z0-9]* ;

COMMENT         : ':O' ~[\r\n]* -> skip ;
COMMENTBLOCK    : ':P' ~[P:]* 'P:' -> skip ;
WS              : [ \t\r\n]+ -> skip ;
NL              : '\r'? '\n' ;
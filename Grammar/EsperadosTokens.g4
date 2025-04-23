lexer grammar Esperados;

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
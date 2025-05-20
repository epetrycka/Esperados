lexer grammar EsperadosTokens;

// LEXER

GREETING        : 'Saluton' ;
GOODBYE         : 'Adiau' ;
PRINT           : 'skribi' ;
INPUT           : 'inputo' ;
VARDEF          : 'variablo' ;
FOREACH         : 'por ciu' ;
IN              : 'en' ;
ELIF            : 'alie se' ;
IF              : 'se' ;
ELSE            : 'alie' ;
FOR             : 'por' ;
WHILE           : 'gis' ;
DEF             : 'difini' ;
DEL             : 'forigi' ;
FUN             : 'funcio' ;

ASG             : 'asigini' ;
ADD             : 'aldoni' ;
SUB             : 'subtrahi' ;
MULT            : 'multigi' ;
DIV             : 'dividi' ;
MOD             : 'modulo' ;
EXPON           : 'intensigi' ;

LP              : '(' ;
RP              : ')' ;

LS              : '[' ;
PS              : ']' ;
LC              : '{' ;
RC              : '}' ;
COMMA           : ',' ;
DOT             : '.' ;
SEMICOLON       : ';' ;
COLON           : ':' ;
EQUALSIGN       : '=' ;

TRUE            : 'vere' ;
FALSE           : 'malvero' ;
BREAK           : 'haltu' ;
CONTINUE        : 'daurigi' ; 
RETURN          : 'reveni' ;

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
LIST            : 'listo' ;

INT             : [0-9]+ ;
fragment ESC    : '\\' ["\\/bfnrt] ;
STRING          : '"' (ESC | ~["\\\r\n])* '"' ;
FLOAT           : [0-9]+ '.' [0-9]+ ;

NAME            : [a-zA-Z] [a-zA-Z0-9_]* ;

COMMENT         : ':O' ~[\r\n]* -> skip ;
COMMENTBLOCK    : ':P' ~[P:]* 'P:' -> skip ;
WS              : [ \t\r\n]+ -> skip ;
NL              : '\r'? '\n' ;
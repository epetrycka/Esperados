grammar Esperados;

//PARSER

program: (comment | NL)* greeting EOF;

comment: COMMENTBLOCK
        | COMMENT
        ;

greeting: GREETING (comment | action | NL)* goodbye?;
goodbye: GOODBYE (comment | NL)* EOF;

action: printExpr
        | variableExpr
        ;

algebraExpr: LP (INT | FLOAT | NAME) (ADD | SUB | MULT | DIV | MOD | EXPON) (INT | FLOAT | NAME) RP;

addStrings: LP STRING ADD STRING RP;

boolExpr: LP expr (EQUAL | INEQUAL | GREATER | LESS | EGREATER | ELESS) expr RP;

expr: (STRING | INT | FLOAT | algebraExpr | NAME | addStrings);

printExpr: PRINT LP (expr | boolExpr) RP;

variableExpr: VARDEF NAME ASS (expr | boolExpr);

// LEXER

GREETING: 'Saluton';
GOODBYE: 'Adiau';
PRINT: 'skribi';
VARDEF: 'variablo';

ASS: 'asigini';
ADD: 'aldoni';
SUB: 'subtrahi';
MULT: 'multigi';
DIV: 'dividi';
MOD: 'modulo';
EXPON: 'intensigi';

LP: '(';
RP: ')';

TRUE: 'vere';
FALSE: 'malvero';
EQUAL: 'egala';
INEQUAL: 'ne egala';
GREATER: 'granda';
LESS: 'malgranda';
EGREATER: 'granda egala';
ELESS: 'malgranda egala';
AND: 'kaj';
OR: 'au';
NOT: 'ne';

INT: [0-9]+;
STRING: '"' [a-zA-Z0-9 ]+ '"';
FLOAT: [0-9]+ '.' [0-9]+;

NAME: [a-zA-Z0-9]+;

COMMENT: ':O' ~[\r\n]* -> skip;
COMMENTBLOCK: ':P' ~[P:]* 'P:' -> skip;
WS: [ \t\r\n]+ -> skip;
NL: '\r'? '\n';
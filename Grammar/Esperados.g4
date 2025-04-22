grammar Esperados;

//PARSER

program: (comment | NL)* GREETING instructions EOF;

comment: (COMMENTBLOCK | COMMENT);

instructions: (comment | action | NL)* goodbye?;
goodbye: GOODBYE (comment | NL)* EOF;

action: (printExpr | variableExpr | condition);
condition: IF LP expr RP LC instructions RC;

algebraExpr: (ADD | SUB | MULT | DIV | MOD | EXPON) (INT | FLOAT | NAME | STRING);

boolExpr: (EQUAL | INEQUAL | GREATER | LESS | EGREATER | ELESS) expr;

logicExpr: (AND | OR) expr;

addStrings: STRING ADD STRING;

expr: ( ((STRING | INT | FLOAT | NAME) addExpr?) | addStrings);

addExpr: (algebraExpr | boolExpr | logicExpr);

printExpr: PRINT LP expr (COMMA expr)* RP;

variableExpr: VARDEF NAME ASS expr;

// LEXER

GREETING: 'Saluton';
GOODBYE: 'Adiau';
PRINT: 'skribi';
VARDEF: 'variablo';
IF: 'se';

ASS: 'asigini';
ADD: 'aldoni';
SUB: 'subtrahi';
MULT: 'multigi';
DIV: 'dividi';
MOD: 'modulo';
EXPON: 'intensigi';

LP: '(';
RP: ')';
LC: '{';
RC: '}';
COMMA: ',';
DOT: '.';

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
fragment ESC: '\\' ["\\/bfnrt];
STRING: '"' (ESC | ~["\\\r\n])* '"';
FLOAT: [0-9]+ '.' [0-9]+;

NAME: [a-zA-Z0-9]+;

COMMENT: ':O' ~[\r\n]* -> skip;
COMMENTBLOCK: ':P' ~[P:]* 'P:' -> skip;
WS: [ \t\r\n]+ -> skip;
NL: '\r'? '\n';
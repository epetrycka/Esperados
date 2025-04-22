grammar Esperados;

//PARSER

program: (comment | NL)* GREETING instructions EOF;

comment: (COMMENTBLOCK | COMMENT);

instructions: (comment | action | NL)* goodbye?;
goodbye: GOODBYE (comment | NL)* EOF;

action: (printExpr | variableExpr | condition);
condition: IF LP expr RP LC instructions RC ;

expr: orExpr ;

orExpr: andExpr (OR andExpr)* ;

andExpr: notExpr (AND notExpr)*;

notExpr: (NOT notExpr | comparisonExpr);

comparisonExpr: additionExpr ( (EQUAL | INEQUAL | GREATER | LESS | EGREATER | ELESS) additionExpr )* ;

additionExpr: multiplicationExpr ( (ADD | SUB) multiplicationExpr )* ;

multiplicationExpr: exponentialExpr ( (MULT | DIV | MOD) exponentialExpr )* ;

exponentialExpr: atom (EXPON atom)* ;

atom: (LP expr RP | INT | FLOAT | STRING | TRUE | FALSE | NAME) ;

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
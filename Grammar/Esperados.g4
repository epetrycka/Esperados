grammar Esperados;

//PARSER

program: GREETING (action|NL)+ GOODBYE EOF;

action: printExpr;

expr: (STRING|INT);
printExpr: PRINT '(' expr ')';

// LEXER

GREETING: 'Saluton';
GOODBYE: 'Adiau';
PRINT: 'skribi';

INT: [0-9]+;
STRING: '"' [a-zA-Z0-9 ]+ '"';

WS: [ \t\r\n]+ -> skip;
NL: '\r'? '\n';
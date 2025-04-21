grammar Esperando;

program: statement+;

statement
    : greeting
    | printStmt
    | goodbye
    ;

greeting: 'Saluton';
goodbye: 'Adiau';
printStmt: 'skribi' '(' STRING ')';

STRING: '"' [a-zA-Z]+ '"';

WS: [ \t\r\n]+ -> skip;

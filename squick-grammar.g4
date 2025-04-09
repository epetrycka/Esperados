grammar squick;

// === Parser Rules ===

program: 'Saluton' statement* 'adiau' EOF ;

statement
    : simpleStatement
    | compoundStatement
    ;

simpleStatement
    : assignment
    | functionCall
    | 'reveni' expr
    | 'haltu'
    | 'daurigi'
    | COMMENT
    ;

compoundStatement
    : ifStatement
    | whileStatement
    | forStatement
    | functionDef
    | tryStatement
    ;

assignment
    : 'variablo' ID 'asigini' expr
    ;

functionDef
    : 'difini' ID '(' parameters? ')' ':' block
    ;

parameters
    : parameter (',' parameter)*
    ;

parameter
    : ID ':' type
    ;

type
    : 'entjero'
    | 'flosi'
    | 'snuro'
    ;

ifStatement
    : 'se' expr ':' block ('alie se' expr ':' block)* ('alie' ':' block)?
    ;

whileStatement
    : 'gis' expr ':' block
    ;

forStatement
    : 'por' ID 'en' expr ':' block
    ;

tryStatement
    : 'provu' ':' block ('krom' ID ':' block)? ('finfine' ':' block)?
    ;

functionCall
    : ID '(' arguments? ')'
    ;

arguments
    : expr (',' expr)*
    ;

block
    : INDENT statement+ DEDENT
    ;

expr
    : expr ('aldoni' | 'subtrahi') expr
    | expr ('multigi' | 'dividi' | 'modulo' | 'intensigi') expr
    | expr ('egala' | 'ne egala' | 'granda' | 'malgranda' | 'Granda egala?' | 'malgranda egala') expr
    | expr ('kaj' | 'au') expr
    | 'ne' expr
    | '(' expr ')'
    | literal
    | ID
    ;

literal
    : INT
    | FLOAT
    | STRING
    | 'malvero'
    | 'vere'
    | 'nenio'
    ;

// === Lexer Rules ===

COMMENT: ':3' ~[\r\n]* -> skip ;

INDENT:
    ;

DEDENT:
    ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
STRING: '"' (~["\\] | '\\' .)* '"' ;

NEWLINE: ('\r'? '\n')+ ;
WS: [ \t]+ -> skip ;

grammar EsperadosExpr;
import EsperadosTokens;

//Definicje wyrażeń

expr            : orExpr ;

orExpr          : andExpr (OR andExpr)* ;

andExpr         : notExpr (AND notExpr)* ;

notExpr         : NOT notExpr
                | comparisonExpr ;

comparisonExpr  : additionExpr ((EQUAL | INEQUAL | GREATER | LESS | EGREATER | ELESS) additionExpr)* ;

additionExpr    : multiExpr ((ADD | SUB) multiExpr)* ;

multiExpr       : exponExpr ((MULT | DIV | MOD) exponExpr)* ;

exponExpr       : atom (EXPON atom)* ;

getFromList     : NAME LS expr PS;

functionCall    : FUN NAME LP (NAME EQUALSIGN expr (COMMA NAME EQUALSIGN expr)*)? RP ;

atom            : LP expr RP
                | INT
                | FLOAT
                | STRING
                | TRUE
                | FALSE
                | NAME 
                | getFromList
                | functionCall;

type            : INTTYPE
                | FLOATTYPE
                | STRINGTYPE 
                | LIST ;

comment         : COMMENTBLOCK 
                | COMMENT ;
grammar Esperados;
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
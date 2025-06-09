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

getFromStruct   : NAME LS expr PS;

functionCall    : FUN NAME LP (NAME EQUALSIGN expr (COMMA NAME EQUALSIGN expr)*)? RP ;

getDictKeys     : KEYS LP NAME RP ;

getDictValues   : VALUES LP NAME RP ;

atom            : LP expr RP
                | INT
                | FLOAT
                | STRING
                | TRUE
                | FALSE
                | NAME 
                | getFromStruct
                | functionCall 
                | getDictKeys 
                | getDictValues ;

type            : INTTYPE
                | FLOATTYPE
                | STRINGTYPE ;

comment         : COMMENTBLOCK 
                | COMMENT ;
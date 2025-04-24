grammar Esperados;
import EsperadosTokens;

defList     : VARDEF NAME ASG LS (expr (COMMA expr)*)? PS;
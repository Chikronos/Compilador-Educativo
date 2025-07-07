lexer grammar AlgoritmosLexer;

LEER: 'leer' ;
IMPRIMIR: 'imprimir' ;
ALGORITMO: 'algoritmo' ;
SI: 'si' ;
SINO: 'sino' ;
MIENTRAS: 'mientras' ;
HACER: 'hacer' ;

LLAVES_ABRE: '{' ;
LLAVES_CIERRA: '}' ;
LPAREN: '(' ;
RPAREN: ')' ;
SEMI: ';' ;
COMMA: ',' ;
ASSIGN: '=' ;
ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;

NUMERO: [0-9]+ ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;

lexer grammar AlgoritmosLexer;

LEER: 'leer' ;
IMPRIMIR: 'imprimir' ;
ALGORITMO: 'algoritmo' ;
LBRACE: '{' ;
RBRACE: '}' ;
LPAREN: '(' ;
RPAREN: ')' ;
SEMI: ';' ;
COMMA: ',' ;
ASSIGN: '=' ;
ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMERO: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;

parser grammar AlgoritmosParser;

options { tokenVocab=AlgoritmosLexer; }

programa
    : ALGORITMO ID LBRACE instrucciones* RBRACE EOF
    ;

instrucciones
    : leer
    | imprimir
    | asignacion
    ;

leer: LEER lista_id SEMI ;

imprimir: IMPRIMIR expresion SEMI ;

asignacion: ID ASSIGN expresion SEMI ;

lista_id: ID (COMMA ID)* ;

expresion
    : expresion op=(ADD | SUB) termino    # SumaResta
    | termino                             # TerminoSolo
    ;

termino
    : termino op=(MUL | DIV) factor       # MulDiv
    | factor                              # FactorSolo
    ;

factor
    : ID                                  # Variable
    | NUMERO                              # Numero
    | LPAREN expresion RPAREN             # Parentesis
    ;

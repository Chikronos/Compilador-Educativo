parser grammar AlgoritmosParser;

options { tokenVocab=AlgoritmosLexer; }

program
    : ALGORITMO ID LLAVES_ABRE instrucciones* LLAVES_CIERRA EOF
    ;

instrucciones
    : leer
    | imprimir
    | asignacion
    | condicion
    | mientras
    ;

leer: LEER lista_id SEMI ;

imprimir: IMPRIMIR expresion SEMI ;

asignacion: ID ASSIGN expresion SEMI ;

// 🔧 NUEVA REGLA: bloque
bloque: LLAVES_ABRE instrucciones* LLAVES_CIERRA ;

condicion
    : SI expresion bloque (SINO bloque)?
    ;

mientras
    : MIENTRAS expresion HACER bloque
    ;

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

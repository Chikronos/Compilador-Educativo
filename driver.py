import sys
from antlr4 import *
from AlgoritmosLexer import AlgoritmosLexer
from AlgoritmosParser import AlgoritmosParser

def main():
    input_stream = FileStream("entrada.alg", encoding="utf-8")
    lexer = AlgoritmosLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = AlgoritmosParser(token_stream)

    tree = parser.programa()  # Llama a la regla de inicio 'program'
    print(tree.toStringTree(recog=parser))  # Muestra el árbol sintáctico

if __name__ == "__main__":
    main()

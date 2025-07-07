from antlr4 import *
from AlgoritmosLexer import AlgoritmosLexer
from AlgoritmosParser import AlgoritmosParser
from visitor import PseudocodigoVisitor

class CompiladorEducativo:
    def __init__(self, archivo):
        self.archivo = archivo

    def analizar(self):
        input_stream = FileStream(self.archivo, encoding="utf-8")
        lexer = AlgoritmosLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = AlgoritmosParser(token_stream)
        tree = parser.program()

        visitor = PseudocodigoVisitor()
        resultado = visitor.visit(tree)
        return resultado

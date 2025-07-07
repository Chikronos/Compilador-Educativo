# Generated from AlgoritmosParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AlgoritmosParser import AlgoritmosParser
else:
    from AlgoritmosParser import AlgoritmosParser

# This class defines a complete generic visitor for a parse tree produced by AlgoritmosParser.

class AlgoritmosParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoritmosParser#program.
    def visitProgram(self, ctx:AlgoritmosParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#instrucciones.
    def visitInstrucciones(self, ctx:AlgoritmosParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#leer.
    def visitLeer(self, ctx:AlgoritmosParser.LeerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#imprimir.
    def visitImprimir(self, ctx:AlgoritmosParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#asignacion.
    def visitAsignacion(self, ctx:AlgoritmosParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#bloque.
    def visitBloque(self, ctx:AlgoritmosParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#condicion.
    def visitCondicion(self, ctx:AlgoritmosParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#mientras.
    def visitMientras(self, ctx:AlgoritmosParser.MientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#lista_id.
    def visitLista_id(self, ctx:AlgoritmosParser.Lista_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#TerminoSolo.
    def visitTerminoSolo(self, ctx:AlgoritmosParser.TerminoSoloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#SumaResta.
    def visitSumaResta(self, ctx:AlgoritmosParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#MulDiv.
    def visitMulDiv(self, ctx:AlgoritmosParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#FactorSolo.
    def visitFactorSolo(self, ctx:AlgoritmosParser.FactorSoloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#Variable.
    def visitVariable(self, ctx:AlgoritmosParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#Numero.
    def visitNumero(self, ctx:AlgoritmosParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmosParser#Parentesis.
    def visitParentesis(self, ctx:AlgoritmosParser.ParentesisContext):
        return self.visitChildren(ctx)



del AlgoritmosParser
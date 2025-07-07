# Generated from AlgoritmosParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,116,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,5,
        0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,42,
        8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        5,5,59,8,5,10,5,12,5,62,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,71,8,
        6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,81,8,8,10,8,12,8,84,9,8,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,92,8,9,10,9,12,9,95,9,9,1,10,1,10,1,10,
        1,10,1,10,1,10,5,10,103,8,10,10,10,12,10,106,9,10,1,11,1,11,1,11,
        1,11,1,11,1,11,3,11,114,8,11,1,11,0,2,18,20,12,0,2,4,6,8,10,12,14,
        16,18,20,22,0,2,1,0,15,16,1,0,17,18,115,0,24,1,0,0,0,2,41,1,0,0,
        0,4,43,1,0,0,0,6,47,1,0,0,0,8,51,1,0,0,0,10,56,1,0,0,0,12,65,1,0,
        0,0,14,72,1,0,0,0,16,77,1,0,0,0,18,85,1,0,0,0,20,96,1,0,0,0,22,113,
        1,0,0,0,24,25,5,3,0,0,25,26,5,20,0,0,26,30,5,8,0,0,27,29,3,2,1,0,
        28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,
        0,0,0,32,30,1,0,0,0,33,34,5,9,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,
        42,3,4,2,0,37,42,3,6,3,0,38,42,3,8,4,0,39,42,3,12,6,0,40,42,3,14,
        7,0,41,36,1,0,0,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,
        1,0,0,0,42,3,1,0,0,0,43,44,5,1,0,0,44,45,3,16,8,0,45,46,5,12,0,0,
        46,5,1,0,0,0,47,48,5,2,0,0,48,49,3,18,9,0,49,50,5,12,0,0,50,7,1,
        0,0,0,51,52,5,20,0,0,52,53,5,14,0,0,53,54,3,18,9,0,54,55,5,12,0,
        0,55,9,1,0,0,0,56,60,5,8,0,0,57,59,3,2,1,0,58,57,1,0,0,0,59,62,1,
        0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,
        64,5,9,0,0,64,11,1,0,0,0,65,66,5,4,0,0,66,67,3,18,9,0,67,70,3,10,
        5,0,68,69,5,5,0,0,69,71,3,10,5,0,70,68,1,0,0,0,70,71,1,0,0,0,71,
        13,1,0,0,0,72,73,5,6,0,0,73,74,3,18,9,0,74,75,5,7,0,0,75,76,3,10,
        5,0,76,15,1,0,0,0,77,82,5,20,0,0,78,79,5,13,0,0,79,81,5,20,0,0,80,
        78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,17,1,0,0,
        0,84,82,1,0,0,0,85,86,6,9,-1,0,86,87,3,20,10,0,87,93,1,0,0,0,88,
        89,10,2,0,0,89,90,7,0,0,0,90,92,3,20,10,0,91,88,1,0,0,0,92,95,1,
        0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,19,1,0,0,0,95,93,1,0,0,0,96,
        97,6,10,-1,0,97,98,3,22,11,0,98,104,1,0,0,0,99,100,10,2,0,0,100,
        101,7,1,0,0,101,103,3,22,11,0,102,99,1,0,0,0,103,106,1,0,0,0,104,
        102,1,0,0,0,104,105,1,0,0,0,105,21,1,0,0,0,106,104,1,0,0,0,107,114,
        5,20,0,0,108,114,5,19,0,0,109,110,5,10,0,0,110,111,3,18,9,0,111,
        112,5,11,0,0,112,114,1,0,0,0,113,107,1,0,0,0,113,108,1,0,0,0,113,
        109,1,0,0,0,114,23,1,0,0,0,8,30,41,60,70,82,93,104,113
    ]

class AlgoritmosParser ( Parser ):

    grammarFileName = "AlgoritmosParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'leer'", "'imprimir'", "'algoritmo'", 
                     "'si'", "'sino'", "'mientras'", "'hacer'", "'{'", "'}'", 
                     "'('", "')'", "';'", "','", "'='", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "LEER", "IMPRIMIR", "ALGORITMO", "SI", 
                      "SINO", "MIENTRAS", "HACER", "LLAVES_ABRE", "LLAVES_CIERRA", 
                      "LPAREN", "RPAREN", "SEMI", "COMMA", "ASSIGN", "ADD", 
                      "SUB", "MUL", "DIV", "NUMERO", "ID", "WS" ]

    RULE_program = 0
    RULE_instrucciones = 1
    RULE_leer = 2
    RULE_imprimir = 3
    RULE_asignacion = 4
    RULE_bloque = 5
    RULE_condicion = 6
    RULE_mientras = 7
    RULE_lista_id = 8
    RULE_expresion = 9
    RULE_termino = 10
    RULE_factor = 11

    ruleNames =  [ "program", "instrucciones", "leer", "imprimir", "asignacion", 
                   "bloque", "condicion", "mientras", "lista_id", "expresion", 
                   "termino", "factor" ]

    EOF = Token.EOF
    LEER=1
    IMPRIMIR=2
    ALGORITMO=3
    SI=4
    SINO=5
    MIENTRAS=6
    HACER=7
    LLAVES_ABRE=8
    LLAVES_CIERRA=9
    LPAREN=10
    RPAREN=11
    SEMI=12
    COMMA=13
    ASSIGN=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    NUMERO=19
    ID=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALGORITMO(self):
            return self.getToken(AlgoritmosParser.ALGORITMO, 0)

        def ID(self):
            return self.getToken(AlgoritmosParser.ID, 0)

        def LLAVES_ABRE(self):
            return self.getToken(AlgoritmosParser.LLAVES_ABRE, 0)

        def LLAVES_CIERRA(self):
            return self.getToken(AlgoritmosParser.LLAVES_CIERRA, 0)

        def EOF(self):
            return self.getToken(AlgoritmosParser.EOF, 0)

        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmosParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(AlgoritmosParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AlgoritmosParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(AlgoritmosParser.ALGORITMO)
            self.state = 25
            self.match(AlgoritmosParser.ID)
            self.state = 26
            self.match(AlgoritmosParser.LLAVES_ABRE)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048662) != 0):
                self.state = 27
                self.instrucciones()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(AlgoritmosParser.LLAVES_CIERRA)
            self.state = 34
            self.match(AlgoritmosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leer(self):
            return self.getTypedRuleContext(AlgoritmosParser.LeerContext,0)


        def imprimir(self):
            return self.getTypedRuleContext(AlgoritmosParser.ImprimirContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(AlgoritmosParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(AlgoritmosParser.CondicionContext,0)


        def mientras(self):
            return self.getTypedRuleContext(AlgoritmosParser.MientrasContext,0)


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = AlgoritmosParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.leer()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.imprimir()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.asignacion()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.condicion()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.mientras()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(AlgoritmosParser.LEER, 0)

        def lista_id(self):
            return self.getTypedRuleContext(AlgoritmosParser.Lista_idContext,0)


        def SEMI(self):
            return self.getToken(AlgoritmosParser.SEMI, 0)

        def getRuleIndex(self):
            return AlgoritmosParser.RULE_leer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeer" ):
                listener.enterLeer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeer" ):
                listener.exitLeer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeer" ):
                return visitor.visitLeer(self)
            else:
                return visitor.visitChildren(self)




    def leer(self):

        localctx = AlgoritmosParser.LeerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_leer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(AlgoritmosParser.LEER)
            self.state = 44
            self.lista_id()
            self.state = 45
            self.match(AlgoritmosParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(AlgoritmosParser.IMPRIMIR, 0)

        def expresion(self):
            return self.getTypedRuleContext(AlgoritmosParser.ExpresionContext,0)


        def SEMI(self):
            return self.getToken(AlgoritmosParser.SEMI, 0)

        def getRuleIndex(self):
            return AlgoritmosParser.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
            else:
                return visitor.visitChildren(self)




    def imprimir(self):

        localctx = AlgoritmosParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(AlgoritmosParser.IMPRIMIR)
            self.state = 48
            self.expresion(0)
            self.state = 49
            self.match(AlgoritmosParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AlgoritmosParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(AlgoritmosParser.ASSIGN, 0)

        def expresion(self):
            return self.getTypedRuleContext(AlgoritmosParser.ExpresionContext,0)


        def SEMI(self):
            return self.getToken(AlgoritmosParser.SEMI, 0)

        def getRuleIndex(self):
            return AlgoritmosParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = AlgoritmosParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(AlgoritmosParser.ID)
            self.state = 52
            self.match(AlgoritmosParser.ASSIGN)
            self.state = 53
            self.expresion(0)
            self.state = 54
            self.match(AlgoritmosParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVES_ABRE(self):
            return self.getToken(AlgoritmosParser.LLAVES_ABRE, 0)

        def LLAVES_CIERRA(self):
            return self.getToken(AlgoritmosParser.LLAVES_CIERRA, 0)

        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmosParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(AlgoritmosParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = AlgoritmosParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(AlgoritmosParser.LLAVES_ABRE)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048662) != 0):
                self.state = 57
                self.instrucciones()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self.match(AlgoritmosParser.LLAVES_CIERRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(AlgoritmosParser.SI, 0)

        def expresion(self):
            return self.getTypedRuleContext(AlgoritmosParser.ExpresionContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmosParser.BloqueContext)
            else:
                return self.getTypedRuleContext(AlgoritmosParser.BloqueContext,i)


        def SINO(self):
            return self.getToken(AlgoritmosParser.SINO, 0)

        def getRuleIndex(self):
            return AlgoritmosParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = AlgoritmosParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(AlgoritmosParser.SI)
            self.state = 66
            self.expresion(0)
            self.state = 67
            self.bloque()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 68
                self.match(AlgoritmosParser.SINO)
                self.state = 69
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(AlgoritmosParser.MIENTRAS, 0)

        def expresion(self):
            return self.getTypedRuleContext(AlgoritmosParser.ExpresionContext,0)


        def HACER(self):
            return self.getToken(AlgoritmosParser.HACER, 0)

        def bloque(self):
            return self.getTypedRuleContext(AlgoritmosParser.BloqueContext,0)


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_mientras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMientras" ):
                listener.enterMientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMientras" ):
                listener.exitMientras(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMientras" ):
                return visitor.visitMientras(self)
            else:
                return visitor.visitChildren(self)




    def mientras(self):

        localctx = AlgoritmosParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(AlgoritmosParser.MIENTRAS)
            self.state = 73
            self.expresion(0)
            self.state = 74
            self.match(AlgoritmosParser.HACER)
            self.state = 75
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AlgoritmosParser.ID)
            else:
                return self.getToken(AlgoritmosParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AlgoritmosParser.COMMA)
            else:
                return self.getToken(AlgoritmosParser.COMMA, i)

        def getRuleIndex(self):
            return AlgoritmosParser.RULE_lista_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_id" ):
                listener.enterLista_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_id" ):
                listener.exitLista_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_id" ):
                return visitor.visitLista_id(self)
            else:
                return visitor.visitChildren(self)




    def lista_id(self):

        localctx = AlgoritmosParser.Lista_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lista_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(AlgoritmosParser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 78
                self.match(AlgoritmosParser.COMMA)
                self.state = 79
                self.match(AlgoritmosParser.ID)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TerminoSoloContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoritmosParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termino(self):
            return self.getTypedRuleContext(AlgoritmosParser.TerminoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminoSolo" ):
                listener.enterTerminoSolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminoSolo" ):
                listener.exitTerminoSolo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminoSolo" ):
                return visitor.visitTerminoSolo(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoritmosParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(AlgoritmosParser.ExpresionContext,0)

        def termino(self):
            return self.getTypedRuleContext(AlgoritmosParser.TerminoContext,0)

        def ADD(self):
            return self.getToken(AlgoritmosParser.ADD, 0)
        def SUB(self):
            return self.getToken(AlgoritmosParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaResta" ):
                listener.enterSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaResta" ):
                listener.exitSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AlgoritmosParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AlgoritmosParser.TerminoSoloContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 86
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AlgoritmosParser.SumaRestaContext(self, AlgoritmosParser.ExpresionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 88
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 89
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 90
                    self.termino(0) 
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_termino

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(TerminoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoritmosParser.TerminoContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def termino(self):
            return self.getTypedRuleContext(AlgoritmosParser.TerminoContext,0)

        def factor(self):
            return self.getTypedRuleContext(AlgoritmosParser.FactorContext,0)

        def MUL(self):
            return self.getToken(AlgoritmosParser.MUL, 0)
        def DIV(self):
            return self.getToken(AlgoritmosParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class FactorSoloContext(TerminoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoritmosParser.TerminoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(AlgoritmosParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorSolo" ):
                listener.enterFactorSolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorSolo" ):
                listener.exitFactorSolo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorSolo" ):
                return visitor.visitFactorSolo(self)
            else:
                return visitor.visitChildren(self)



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AlgoritmosParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_termino, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AlgoritmosParser.FactorSoloContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 97
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AlgoritmosParser.MulDivContext(self, AlgoritmosParser.TerminoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                    self.state = 99
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 100
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==17 or _la==18):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 101
                    self.factor() 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumeroContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoritmosParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(AlgoritmosParser.NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoritmosParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AlgoritmosParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AlgoritmosParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AlgoritmosParser.LPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(AlgoritmosParser.ExpresionContext,0)

        def RPAREN(self):
            return self.getToken(AlgoritmosParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = AlgoritmosParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = AlgoritmosParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(AlgoritmosParser.ID)
                pass
            elif token in [19]:
                localctx = AlgoritmosParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(AlgoritmosParser.NUMERO)
                pass
            elif token in [10]:
                localctx = AlgoritmosParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(AlgoritmosParser.LPAREN)
                self.state = 110
                self.expresion(0)
                self.state = 111
                self.match(AlgoritmosParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expresion_sempred
        self._predicates[10] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         





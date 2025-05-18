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
        4,1,17,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,0,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,52,8,5,10,5,12,5,55,9,5,1,6,
        1,6,1,6,1,6,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,7,1,7,1,7,1,7,
        1,7,1,7,5,7,74,8,7,10,7,12,7,77,9,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        85,8,8,1,8,0,2,12,14,9,0,2,4,6,8,10,12,14,16,0,2,1,0,11,12,1,0,13,
        14,85,0,18,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,39,1,0,0,0,8,43,1,
        0,0,0,10,48,1,0,0,0,12,56,1,0,0,0,14,67,1,0,0,0,16,84,1,0,0,0,18,
        19,5,3,0,0,19,20,5,15,0,0,20,24,5,4,0,0,21,23,3,2,1,0,22,21,1,0,
        0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,24,
        1,0,0,0,27,28,5,5,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,34,3,4,2,0,31,
        34,3,6,3,0,32,34,3,8,4,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,
        0,34,3,1,0,0,0,35,36,5,1,0,0,36,37,3,10,5,0,37,38,5,8,0,0,38,5,1,
        0,0,0,39,40,5,2,0,0,40,41,3,12,6,0,41,42,5,8,0,0,42,7,1,0,0,0,43,
        44,5,15,0,0,44,45,5,10,0,0,45,46,3,12,6,0,46,47,5,8,0,0,47,9,1,0,
        0,0,48,53,5,15,0,0,49,50,5,9,0,0,50,52,5,15,0,0,51,49,1,0,0,0,52,
        55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,11,1,0,0,0,55,53,1,0,0,
        0,56,57,6,6,-1,0,57,58,3,14,7,0,58,64,1,0,0,0,59,60,10,2,0,0,60,
        61,7,0,0,0,61,63,3,14,7,0,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,
        0,0,64,65,1,0,0,0,65,13,1,0,0,0,66,64,1,0,0,0,67,68,6,7,-1,0,68,
        69,3,16,8,0,69,75,1,0,0,0,70,71,10,2,0,0,71,72,7,1,0,0,72,74,3,16,
        8,0,73,70,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,15,
        1,0,0,0,77,75,1,0,0,0,78,85,5,15,0,0,79,85,5,16,0,0,80,81,5,6,0,
        0,81,82,3,12,6,0,82,83,5,7,0,0,83,85,1,0,0,0,84,78,1,0,0,0,84,79,
        1,0,0,0,84,80,1,0,0,0,85,17,1,0,0,0,6,24,33,53,64,75,84
    ]

class AlgoritmosParser ( Parser ):

    grammarFileName = "AlgoritmosParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'leer'", "'imprimir'", "'algoritmo'", 
                     "'{'", "'}'", "'('", "')'", "';'", "','", "'='", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "LEER", "IMPRIMIR", "ALGORITMO", "LBRACE", 
                      "RBRACE", "LPAREN", "RPAREN", "SEMI", "COMMA", "ASSIGN", 
                      "ADD", "SUB", "MUL", "DIV", "ID", "NUMERO", "WS" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_leer = 2
    RULE_imprimir = 3
    RULE_asignacion = 4
    RULE_lista_id = 5
    RULE_expresion = 6
    RULE_termino = 7
    RULE_factor = 8

    ruleNames =  [ "programa", "instrucciones", "leer", "imprimir", "asignacion", 
                   "lista_id", "expresion", "termino", "factor" ]

    EOF = Token.EOF
    LEER=1
    IMPRIMIR=2
    ALGORITMO=3
    LBRACE=4
    RBRACE=5
    LPAREN=6
    RPAREN=7
    SEMI=8
    COMMA=9
    ASSIGN=10
    ADD=11
    SUB=12
    MUL=13
    DIV=14
    ID=15
    NUMERO=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALGORITMO(self):
            return self.getToken(AlgoritmosParser.ALGORITMO, 0)

        def ID(self):
            return self.getToken(AlgoritmosParser.ID, 0)

        def LBRACE(self):
            return self.getToken(AlgoritmosParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(AlgoritmosParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(AlgoritmosParser.EOF, 0)

        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AlgoritmosParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(AlgoritmosParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = AlgoritmosParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(AlgoritmosParser.ALGORITMO)
            self.state = 19
            self.match(AlgoritmosParser.ID)
            self.state = 20
            self.match(AlgoritmosParser.LBRACE)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32774) != 0):
                self.state = 21
                self.instrucciones()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(AlgoritmosParser.RBRACE)
            self.state = 28
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


        def getRuleIndex(self):
            return AlgoritmosParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)




    def instrucciones(self):

        localctx = AlgoritmosParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.leer()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.imprimir()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.asignacion()
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




    def leer(self):

        localctx = AlgoritmosParser.LeerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_leer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(AlgoritmosParser.LEER)
            self.state = 36
            self.lista_id()
            self.state = 37
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




    def imprimir(self):

        localctx = AlgoritmosParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(AlgoritmosParser.IMPRIMIR)
            self.state = 40
            self.expresion(0)
            self.state = 41
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




    def asignacion(self):

        localctx = AlgoritmosParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(AlgoritmosParser.ID)
            self.state = 44
            self.match(AlgoritmosParser.ASSIGN)
            self.state = 45
            self.expresion(0)
            self.state = 46
            self.match(AlgoritmosParser.SEMI)
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




    def lista_id(self):

        localctx = AlgoritmosParser.Lista_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lista_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(AlgoritmosParser.ID)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 49
                self.match(AlgoritmosParser.COMMA)
                self.state = 50
                self.match(AlgoritmosParser.ID)
                self.state = 55
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



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AlgoritmosParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AlgoritmosParser.TerminoSoloContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 57
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AlgoritmosParser.SumaRestaContext(self, AlgoritmosParser.ExpresionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 59
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 60
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 61
                    self.termino(0) 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AlgoritmosParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_termino, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AlgoritmosParser.FactorSoloContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 68
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AlgoritmosParser.MulDivContext(self, AlgoritmosParser.TerminoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                    self.state = 70
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 71
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 72
                    self.factor() 
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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



    def factor(self):

        localctx = AlgoritmosParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = AlgoritmosParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(AlgoritmosParser.ID)
                pass
            elif token in [16]:
                localctx = AlgoritmosParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(AlgoritmosParser.NUMERO)
                pass
            elif token in [6]:
                localctx = AlgoritmosParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(AlgoritmosParser.LPAREN)
                self.state = 81
                self.expresion(0)
                self.state = 82
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
        self._predicates[6] = self.expresion_sempred
        self._predicates[7] = self.termino_sempred
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
         





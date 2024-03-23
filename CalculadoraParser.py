# Generated from Calculadora.g4 by ANTLR 4.13.1
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
        4,1,16,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,30,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,46,8,4,1,4,0,0,5,0,2,4,6,8,0,0,48,0,10,1,0,0,0,2,18,
        1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,8,45,1,0,0,0,10,15,3,2,1,0,11,
        12,5,11,0,0,12,14,3,2,1,0,13,11,1,0,0,0,14,17,1,0,0,0,15,13,1,0,
        0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,15,1,0,0,0,18,19,3,4,2,0,19,3,
        1,0,0,0,20,30,5,14,0,0,21,22,5,1,0,0,22,23,3,4,2,0,23,24,3,4,2,0,
        24,25,5,3,0,0,25,26,5,2,0,0,26,30,1,0,0,0,27,30,3,6,3,0,28,30,3,
        8,4,0,29,20,1,0,0,0,29,21,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,
        5,1,0,0,0,31,32,5,1,0,0,32,33,3,4,2,0,33,34,5,12,0,0,34,35,5,2,0,
        0,35,7,1,0,0,0,36,37,5,1,0,0,37,38,3,4,2,0,38,39,5,13,0,0,39,40,
        5,2,0,0,40,46,1,0,0,0,41,46,5,13,0,0,42,43,5,1,0,0,43,44,5,13,0,
        0,44,46,5,2,0,0,45,36,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,46,9,1,
        0,0,0,3,15,29,45
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'|'", "'/'", "'%'", "'^'", "'\\n'", "'RES'", 
                     "'MEM'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SYMBOL", "SUM", 
                      "SUBTRACTION", "MULTIPLY", "DIVISION", "INTEGER_DIVISION", 
                      "MODULO", "POTENTIATION", "ENTER", "RES", "MEM", "NUMBER", 
                      "INTEGER", "WS" ]

    RULE_start = 0
    RULE_line = 1
    RULE_number = 2
    RULE_res = 3
    RULE_mem = 4

    ruleNames =  [ "start", "line", "number", "res", "mem" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SYMBOL=3
    SUM=4
    SUBTRACTION=5
    MULTIPLY=6
    DIVISION=7
    INTEGER_DIVISION=8
    MODULO=9
    POTENTIATION=10
    ENTER=11
    RES=12
    MEM=13
    NUMBER=14
    INTEGER=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.LineContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.LineContext,i)


        def ENTER(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.ENTER)
            else:
                return self.getToken(CalculadoraParser.ENTER, i)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = CalculadoraParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.line()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 11
                self.match(CalculadoraParser.ENTER)
                self.state = 12
                self.line()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(CalculadoraParser.NumberContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = CalculadoraParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CalculadoraParser.NUMBER, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.NumberContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.NumberContext,i)


        def SYMBOL(self):
            return self.getToken(CalculadoraParser.SYMBOL, 0)

        def res(self):
            return self.getTypedRuleContext(CalculadoraParser.ResContext,0)


        def mem(self):
            return self.getTypedRuleContext(CalculadoraParser.MemContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = CalculadoraParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_number)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(CalculadoraParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(CalculadoraParser.T__0)
                self.state = 22
                self.number()
                self.state = 23
                self.number()
                self.state = 24
                self.match(CalculadoraParser.SYMBOL)
                self.state = 25
                self.match(CalculadoraParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.res()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.mem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(CalculadoraParser.NumberContext,0)


        def RES(self):
            return self.getToken(CalculadoraParser.RES, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_res

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRes" ):
                listener.enterRes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRes" ):
                listener.exitRes(self)




    def res(self):

        localctx = CalculadoraParser.ResContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_res)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(CalculadoraParser.T__0)
            self.state = 32
            self.number()
            self.state = 33
            self.match(CalculadoraParser.RES)
            self.state = 34
            self.match(CalculadoraParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(CalculadoraParser.NumberContext,0)


        def MEM(self):
            return self.getToken(CalculadoraParser.MEM, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_mem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMem" ):
                listener.enterMem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMem" ):
                listener.exitMem(self)




    def mem(self):

        localctx = CalculadoraParser.MemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mem)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.match(CalculadoraParser.T__0)
                self.state = 37
                self.number()
                self.state = 38
                self.match(CalculadoraParser.MEM)
                self.state = 39
                self.match(CalculadoraParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(CalculadoraParser.MEM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(CalculadoraParser.T__0)
                self.state = 43
                self.match(CalculadoraParser.MEM)
                self.state = 44
                self.match(CalculadoraParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






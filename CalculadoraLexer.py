#Gabriel Barros, Guilherme Ramos, Matheus Romeike
# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,95,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,45,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,3,13,
        72,8,13,1,13,4,13,75,8,13,11,13,12,13,76,1,13,1,13,4,13,81,8,13,
        11,13,12,13,82,3,13,85,8,13,1,14,1,14,1,15,4,15,90,8,15,11,15,12,
        15,91,1,15,1,15,0,0,16,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,1,0,2,1,0,48,57,3,0,9,9,13,
        13,32,32,105,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,
        1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,
        1,0,0,0,0,31,1,0,0,0,1,33,1,0,0,0,3,35,1,0,0,0,5,44,1,0,0,0,7,46,
        1,0,0,0,9,48,1,0,0,0,11,50,1,0,0,0,13,52,1,0,0,0,15,54,1,0,0,0,17,
        56,1,0,0,0,19,58,1,0,0,0,21,60,1,0,0,0,23,62,1,0,0,0,25,66,1,0,0,
        0,27,71,1,0,0,0,29,86,1,0,0,0,31,89,1,0,0,0,33,34,5,40,0,0,34,2,
        1,0,0,0,35,36,5,41,0,0,36,4,1,0,0,0,37,45,3,7,3,0,38,45,3,9,4,0,
        39,45,3,11,5,0,40,45,3,13,6,0,41,45,3,15,7,0,42,45,3,17,8,0,43,45,
        3,19,9,0,44,37,1,0,0,0,44,38,1,0,0,0,44,39,1,0,0,0,44,40,1,0,0,0,
        44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,6,1,0,0,0,46,47,5,43,
        0,0,47,8,1,0,0,0,48,49,5,45,0,0,49,10,1,0,0,0,50,51,5,42,0,0,51,
        12,1,0,0,0,52,53,5,124,0,0,53,14,1,0,0,0,54,55,5,47,0,0,55,16,1,
        0,0,0,56,57,5,37,0,0,57,18,1,0,0,0,58,59,5,94,0,0,59,20,1,0,0,0,
        60,61,5,10,0,0,61,22,1,0,0,0,62,63,5,82,0,0,63,64,5,69,0,0,64,65,
        5,83,0,0,65,24,1,0,0,0,66,67,5,77,0,0,67,68,5,69,0,0,68,69,5,77,
        0,0,69,26,1,0,0,0,70,72,5,45,0,0,71,70,1,0,0,0,71,72,1,0,0,0,72,
        74,1,0,0,0,73,75,3,29,14,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,
        0,0,76,77,1,0,0,0,77,84,1,0,0,0,78,80,5,46,0,0,79,81,3,29,14,0,80,
        79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,
        0,84,78,1,0,0,0,84,85,1,0,0,0,85,28,1,0,0,0,86,87,7,0,0,0,87,30,
        1,0,0,0,88,90,7,1,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,89,1,0,0,0,
        91,92,1,0,0,0,92,93,1,0,0,0,93,94,6,15,0,0,94,32,1,0,0,0,7,0,44,
        71,76,82,84,91,1,6,0,0
    ]

class CalculadoraLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    SYMBOL = 3
    SUM = 4
    SUBTRACTION = 5
    MULTIPLY = 6
    DIVISION = 7
    INTEGER_DIVISION = 8
    MODULO = 9
    POTENTIATION = 10
    ENTER = 11
    RES = 12
    MEM = 13
    NUMBER = 14
    INTEGER = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "'|'", "'/'", "'%'", "'^'", 
            "'\\n'", "'RES'", "'MEM'" ]

    symbolicNames = [ "<INVALID>",
            "SYMBOL", "SUM", "SUBTRACTION", "MULTIPLY", "DIVISION", "INTEGER_DIVISION", 
            "MODULO", "POTENTIATION", "ENTER", "RES", "MEM", "NUMBER", "INTEGER", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "SYMBOL", "SUM", "SUBTRACTION", "MULTIPLY", 
                  "DIVISION", "INTEGER_DIVISION", "MODULO", "POTENTIATION", 
                  "ENTER", "RES", "MEM", "NUMBER", "INTEGER", "WS" ]

    grammarFileName = "Calculadora.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



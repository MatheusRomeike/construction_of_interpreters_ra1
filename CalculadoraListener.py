# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):
    pilha = []
    pilhaArquivo = []
    memoria = 0.0

    def resolve(self, op, a, b):

        result = 0

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '|':
            if b == 0:
                raise Exception("Division by zero")
            result = a / b
        elif op == '/':
            if b == 0:
                raise Exception("Division by zero")
            result = a // b
        elif op == '%':
            if b == 0:
                raise Exception("Division by zero")
            result = a % b
        elif op == '^':
            if (b < 0 or b != round(b, 0)):
                raise Exception("Negative or not integer exponentiation")
            result = a ** b

        return round(result, 2)

    # Enter a parse tree produced by CalculadoraParser#start.
    def enterStart(self, ctx:CalculadoraParser.StartContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#start.
    def exitStart(self, ctx:CalculadoraParser.StartContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#line.
    def enterLine(self, ctx:CalculadoraParser.LineContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#line.
    def exitLine(self, ctx:CalculadoraParser.LineContext):
        self.pilhaArquivo.append(self.pilha.pop())
        pass


    # Enter a parse tree produced by CalculadoraParser#expression.
    def enterExpression(self, ctx:CalculadoraParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#expression.
    def exitExpression(self, ctx:CalculadoraParser.ExpressionContext):
        symbol = ctx.SYMBOL()
        number = ctx.NUMBER()
        if symbol:
            symbol = symbol.getText()
            b = self.pilha.pop()
            a = self.pilha.pop()
            result = self.resolve(symbol, a, b)
            self.pilha.append(result)

        elif number:
            self.pilha.append(float(number.getText()))

        pass


    # Enter a parse tree produced by CalculadoraParser#res.
    def enterRes(self, ctx:CalculadoraParser.ResContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#res.
    def exitRes(self, ctx:CalculadoraParser.ResContext):
        index = self.pilha.pop()
        if (index < 0 or index != round(index, 0)):
                raise Exception("Negative or not integer index")
        if len(self.pilhaArquivo) < int(index):
            raise Exception("Invalid memory access")
        self.pilha.append(self.pilhaArquivo[int(index) - 1])
        pass


    # Enter a parse tree produced by CalculadoraParser#mem.
    def enterMem(self, ctx:CalculadoraParser.MemContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#mem.
    def exitMem(self, ctx:CalculadoraParser.MemContext):
        try:
            expression = ctx.expression().getText()
        except:
            expression = None

        if expression:
            self.memoria = float(self.pilha.pop())

        self.pilha.append(self.memoria)
        pass



del CalculadoraParser
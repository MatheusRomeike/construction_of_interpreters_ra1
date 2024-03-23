#Gabriel Barros, Guilherme Ramos, Matheus Romeike
# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):
    stack = []
    stackFile = []
    memory = 0.0

    def resolve(self, op, a, b):

        result = 0

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '|':
            #If the number is negative, it is an invalid operation
            if b == 0:
                raise Exception("Division by zero")
            result = a / b
        elif op == '/':
            #If the number is negative, it is an invalid operation
            if b == 0:
                raise Exception("Division by zero")
            result = a // b
        elif op == '%':
            #If the number is negative, it is an invalid operation
            if b == 0:
                raise Exception("Division by zero")
            result = a % b
        elif op == '^':
            #If the number is negative or not an integer, it is an invalid operation
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
        self.stackFile.append(self.stack.pop())
        pass


    # Enter a parse tree produced by CalculadoraParser#expression.
    def enterExpression(self, ctx:CalculadoraParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#expression.
    def exitExpression(self, ctx:CalculadoraParser.ExpressionContext):
        symbol = ctx.SYMBOL()
        number = ctx.NUMBER()

        #If there is a symbol, it is an operation
        if symbol:
            symbol = symbol.getText()
            b = self.stack.pop()
            a = self.stack.pop()
            result = self.resolve(symbol, a, b)
            self.stack.append(result)
        #If there is a number, it is a value
        elif number:
            self.stack.append(float(number.getText()))

        pass


    # Enter a parse tree produced by CalculadoraParser#res.
    def enterRes(self, ctx:CalculadoraParser.ResContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#res.
    def exitRes(self, ctx:CalculadoraParser.ResContext):
        index = self.stack.pop()
        #If the index is negative or not an integer, it is an invalid memory access
        if (index < 0 or index != round(index, 0)):
                raise Exception("Negative or not integer index")
        #If the index is greater than the number of elements in the file, it is an invalid memory access
        if len(self.stackFile) < int(index):
            raise Exception("Invalid memory access")
        self.stack.append(self.stackFile[int(index) - 1])
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
            self.memory = float(self.stack.pop())

        self.stack.append(self.memory)
        pass



del CalculadoraParser
import sys
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraListener import CalculadoraListener

def main(argv):
    file_stream = FileStream('input.txt')
    lexer = CalculadoraLexer(file_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculadoraParser(stream)
    listener = CalculadoraListener()
    tree = parser.start()
    
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
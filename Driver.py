#Gabriel Barros, Guilherme Ramos, Matheus Romeike
import sys
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraListener import CalculadoraListener

def main(argv):
    # Check if the file name was passed as an argument
    if(len(argv)<= 1):
        raise Exception("Missing file name")
    fileName = f"{sys.argv[1]}.txt"
    file_stream = FileStream(fileName)
    lexer = CalculadoraLexer(file_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculadoraParser(stream)
    listener = CalculadoraListener()
    tree = parser.start()
    
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
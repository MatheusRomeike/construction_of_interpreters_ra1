#Gabriel Barros, Guilherme Ramos, Matheus Romeike
import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraListener import CalculadoraListener

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol is not None:
            raise Exception(f"Lexer error at line {line}, column {column}: {msg}")
        else:
            raise Exception(f"Lexer error at line {line}, column {column}")


def main(argv):
    # Check if the file name was passed as an argument
    if(len(argv)<= 1):
        raise Exception("Missing file name")
    fileName = f"{sys.argv[1]}.txt"
    file_stream = FileStream(fileName)
    lexer = CalculadoraLexer(file_stream)
    lexer.removeErrorListeners()  # Remove os listeners de erro padrão
    lexer.addErrorListener(ThrowingErrorListener())  # Adiciona um listener de erro que irá lançar exceções

    token_stream = CommonTokenStream(lexer)
    parser = CalculadoraParser(token_stream)
    parser.removeErrorListeners()  # Remove os listeners de erro padrão
    parser.addErrorListener(ThrowingErrorListener())  # Adiciona um listener de erro que irá lançar exceções

    tree = parser.start()

    print("Tree parser:")
    print_tree(tree, parser)

    errors = parser.getNumberOfSyntaxErrors()
    if errors == 0:
        print("The code has no syntax errors.")
    else:
        print(f"The code has {errors} syntax errors.")
        sys.exit(1)

    listener = CalculadoraListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

def print_tree(tree, parser, indent='   '):
    if tree.getChildCount() == 0:
        print(indent + tree.getText())
    else:
        rule_name = parser.ruleNames[tree.getRuleIndex()]
        if rule_name == "line":
            print("line: " + indent)
        else:
            print(indent + rule_name )
        for child in tree.children:
            print_tree(child, parser, indent + '        ')

if __name__ == '__main__':
    main(sys.argv)
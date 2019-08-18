from antlr4 import *
from arithmetic_grammarLexer import arithmetic_grammarLexer
from arithmetic_grammarListener import arithmetic_grammarListener
from arithmetic_grammarParser import arithmetic_grammarParser
import sys
import argparse

class arithmetic_grammarPrintListener(arithmetic_grammarListener):
    def enterHi(self, ctx):
        print("arithmetic_grammar: %s" % ctx.ID())

def main():
    lexer = arithmetic_grammarLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = arithmetic_grammarParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    printer = arithmetic_grammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()


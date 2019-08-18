from antlr4 import *
from number_grammarLexer import number_grammarLexer
from number_grammarListener import number_grammarListener
from number_grammarParser import number_grammarParser
import sys
import argparse

class number_grammarPrintListener(number_grammarListener):
    def enterHi(self, ctx):
        print("number_grammar: %s" % ctx.ID())

def main():
    lexer = number_grammarLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = number_grammarParser(stream)
    tree = parser.number()
    print(tree.toStringTree(recog=parser))
    printer = number_grammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()


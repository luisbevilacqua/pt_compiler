from antlr4 import *
from PtGrammarLexer import PtGrammarLexer
from PtGrammarListener import PtGrammarListener
from PtGrammarParser import PtGrammarParser
import sys
import argparse

class PtGrammarPrintListener(PtGrammarListener):
    def enterHi(self, ctx):
        print("PtGrammar: %s" % ctx.ID())

def main():
    lexer = PtGrammarLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = PtGrammarParser(stream)
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))
    printer = PtGrammarPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()


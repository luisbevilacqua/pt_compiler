from antlr4 import *
from PtGrammarLexer import PtGrammarLexer
from PtGrammarListenerJava import PtGrammarListenerJava
from PtGrammarListenerC import PtGrammarListenerC
from PtGrammarParser import PtGrammarParser
import sys
import argparse


class PTCompiler():

    def __init__(self, language, input_file=None, output_file=None):
        self.input_file = input_file 
        self.output_file = output_file 
        self.language = language
        self.stream = self.get_pt_code()
        self.listener = self.get_listener()

    def get_pt_code(self):
        if self.input_file:
            try:
                with open(self.input_file, 'r') as pt_file:
                    file_content = pt_file.read()
                stream = InputStream(file_content)
            except FileNotFoundError as e:
                print(f"The file does not exist: {self.input_file}")
                raise(e)
        else:
            print("Companheiro, insert the code that you want to compile. ")
            stream = StdinStream()
        return stream
    

    def get_listener(self):
        if self.language == 'c':
            listener = PtGrammarListenerC
        elif self.language == 'java':
            listener = PtGrammarListenerJava
        else:
            raise NotImplementedError(
                "The parser for this language does not exist!"
            )
        return listener


    def compile(self):
        lexer = PtGrammarLexer(self.stream)
        stream = CommonTokenStream(lexer)
        parser = PtGrammarParser(stream)
        tree = parser.programa()
        printer = self.listener(self.output_file)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)


def get_args():
    parser = argparse.ArgumentParser(
        description='Compile programs in PT Language to C or Java.'
    )
    parser.add_argument(
        '--input_file', 
        help=(
            "Path to PT file to compile. "
            "If not specified, the code should be written in the terminal."
        )
    )
    parser.add_argument(
        '--output_file', 
        help=(
            "Path to file to store the compiled PT program. "
            "If not specified, the code will be written in the terminal."
        )
    )
    parser.add_argument(
        'language', 
        help="Language target to compile the PT code to.",
        choices=['java', 'c']
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    compiler = PTCompiler(**vars(args))
    compiler.compile()


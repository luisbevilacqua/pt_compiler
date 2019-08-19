from antlr4 import *
from PtGrammarLexer import PtGrammarLexer
from PtGrammarListener import PtGrammarListener
from PtGrammarParser import PtGrammarParser
import sys
import argparse


def get_file_content(filepath):
    try:
        with open(filepath, 'r') as pt_file:
            content = pt_file.read()
    except FileNotFoundError as e:
        print(f"The file does not exist: {filepath}")
        raise(e)
    else:
        return content
    

def compile(input_file, output_file, language):
    if input_file:
        file_content = get_file_content(input_file)
        lexer = PtGrammarLexer(InputStream(file_content))
    else:
        lexer = PtGrammarLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = PtGrammarParser(stream)
    tree = parser.programa()
    printer = PtGrammarListener(language, output_file)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


def main(args):
    input_file = args.input_file
    output_file = args.output_file
    language = args.language
    if input_file:
        content = get_file_content(input_file)
    else: 
        content=None
    
    compile(input_file, output_file, language)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compile programs in PT Language to Java.'
    )
    parser.add_argument(
        '--input_file', 
        help='Path to PT file to compile.'
    )
    parser.add_argument(
        '--output_file', 
        help='Path to PT file to compile.'
    )
    parser.add_argument(
        '--language', 
        help='Language target to compile the PT code.',
        choices=['java', 'c'],
        default='c'
    )
    args = parser.parse_args()

    main(args)

"""
    This is the main implementation of the PL Language Compiler.
    Here we will use all other modules to compile and run the program.
    (c) 2024|1403
"""
import argparse
from argparse import ArgumentParser
from lexical_analyzer.tokenizer import tokenize
from token_printer import print_tokens, write_to_file


def main(source, output, debug=False, with_ws=False):
    """
    This is the main implementation of the PL Language Compiler.
    :param source: this is address of the source file.
    :param debug: this flag will enable debug mode.
    :param with_ws: this flag is used for print mode of debug.
    :return:
    """
    with open(source, "r") as file:
        program = file.read()
    tokens = tokenize(program)

    write_to_file(tokens, filename=output, with_ws_print=with_ws)

    if debug:
        print_tokens(tokens, with_ws_print=with_ws)


if __name__ == '__main__':
    """
    Here is the entry point of the program. First the possible arguments will be parsed,
    and then the program will read the source code and compile it.
    """
    parser = ArgumentParser(description='PL Compiler')
    parser.add_argument('--source', default='./lexical_analyzer/test/test.c', type=str,
                        help='Input Program Address')
    parser.add_argument('--output', default='./lexical_analyzer/test/result.txt', type=str,
                        help='Output Program Address')
    parser.add_argument('--debug', default=False, action=argparse.BooleanOptionalAction,
                        help='it will show debugging info')
    parser.add_argument('--with-ws', default=False, action=argparse.BooleanOptionalAction,
                        help='it will print the whitespaces')

    args = parser.parse_args()
    SOURCE = args.source
    OUTPUT = args.output
    DEBUG = args.debug
    WITH_WS = args.with_ws

    main(SOURCE, OUTPUT, DEBUG, WITH_WS)

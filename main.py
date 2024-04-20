"""
    This is the main implementation of the PL Language Compiler.
    Here we will use all other modules to compile and run the program.
    (c) 2024|1403
"""
from argparse import ArgumentParser
from lexical_analyzer.tokenizer import tokenize
from token_printer import print_tokens


def main(source, debug=False, with_ws=False):
    # TODO: Fix reading from file
    with open(source, "r") as file:
        program = file.read()
    tokens = tokenize(program)

    if(debug):
        print_tokens(tokens, with_ws_print=with_ws)


if __name__ == '__main__':
    """
    Here is the entry point of the program. First the possible arguments will be parsed,
    and then the program will read the source code and compile it.
    """
    parser = ArgumentParser(description='PL Compiler')
    parser.add_argument('--source', default='./lexical_analyzer/test/test.c', type=str, help='Input Program Address')
    parser.add_argument('--debug', default='True', type=str, help='If True, it will show debugging info')
    parser.add_argument('--with-ws', default='True', type=str, help='If True, it will print the withspaces')

    args = parser.parse_args()
    SOURCE = args.source
    DEBUG = True if args.debug == 'True' else False
    WITH_WS = True if args.with_ws == 'True' else False

    main(SOURCE, DEBUG, WITH_WS)


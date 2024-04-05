"""
    This is the main implementation of the PL Language Compiler.
    Here we will use all other modules to compile and run the program.
    (c) 2024|1403
"""
from argparse import ArgumentParser
from lexical_analyzer.tokenizer import tokenize


def main(source, debug=False):
    with open(source, "r") as file:
        program = file.read()
    tokens = tokenize(program)


if __name__ == '__main__':
    """
    Here is the entry point of the program. First the possible arguments will be parsed,
    and then the program will read the source code and compile it.
    """
    parser = ArgumentParser(description='PL Compiler')
    parser.add_argument('--source', default='./*.pl', type=str, help='Input Program Address')
    parser.add_argument('--debug', default='True', type=str, help='If True it will show debugging info')

    args = parser.parse_args()
    SOURCE = args.source
    DEBUG = args.debug
    main(SOURCE, DEBUG)


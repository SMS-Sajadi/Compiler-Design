"""
    This is the main implementation of the PL Language Compiler.
    Here we will use all other modules to compile and run the program.
    (c) 2024|1403
"""
import argparse
from argparse import ArgumentParser
from lexical_analyzer.tokenizer import tokenize
from lexical_analyzer.comment_ws_remover import remove
from token_printer import print_tokens, write_to_file
from syntax_analyzer.parser import parse
from syntax_analyzer.error_handlers import set_program
from tree_printer import print_tree, write_tree_to_file


def main(source, output, debug=False, with_ws=False, tree_print=True, graphic_print=False):
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

    write_to_file(tokens, address=output, with_ws_print=with_ws)

    set_program(program)
    tokens = remove(tokens)
    tree = parse(tokens)

    write_tree_to_file(tree, address=output)

    if debug:
        print_tokens(tokens, with_ws_print=with_ws)
    if tree_print:
        print_tree(tree, address=output, graphic_print=graphic_print)


if __name__ == '__main__':
    """
    Here is the entry point of the program. First the possible arguments will be parsed,
    and then the program will read the source code and compile it.
    """
    parser = ArgumentParser(description='PL Compiler')
    parser.add_argument('--source', default='./test/test.c', type=str,
                        help='Input Program Address')
    parser.add_argument('--output', default='./test/output', type=str,
                        help='Program Output Directory Address')
    parser.add_argument('--debug', default=False, action=argparse.BooleanOptionalAction,
                        help='it will show debugging info')
    parser.add_argument('--with-ws', default=True, action=argparse.BooleanOptionalAction,
                        help='it will print the whitespaces')
    parser.add_argument('--tree_printing', default=True, action=argparse.BooleanOptionalAction,
                        help='it will print the syntax tree')
    parser.add_argument('--graphic', default=True, action=argparse.BooleanOptionalAction,
                        help='it will print the syntax tree graphically')

    args = parser.parse_args()
    SOURCE = args.source
    OUTPUT = args.output
    DEBUG = args.debug
    WITH_WS = args.with_ws
    TREE_PRINTING = args.tree_printing
    GRAPHIC = args.graphic

    main(SOURCE, OUTPUT, DEBUG, WITH_WS, TREE_PRINTING, GRAPHIC)

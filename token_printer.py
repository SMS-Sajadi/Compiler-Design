"""
    This file is used for pretty printing tokens.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from lexical_analyzer.token_base import Token


def print_tokens(tokens: List[Token], *, with_ws_print: bool =True) -> None:
    """
    This Function will print the tokens in lexical analyzer.
    :param tokens: List of tokens.
    :param with_ws_print: If it is true, the withspaces will be printed.
    :return:
    """
    if with_ws_print:
        print(*tokens, sep='\n')
    else:
        for token in tokens:
            if token.type != "T_Whitespace":
                print(token)

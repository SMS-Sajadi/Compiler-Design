"""
    This file is used for cleaning up tokens.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from lexical_analyzer.token_base import Token


def remove(tokens: List[Token]) -> List[Token]:
    """
    Remove all comments ans whitespaces from a list of tokens.
    :param tokens:
    :return:
    """
    for idx in range(len(tokens) - 1, -1, -1):
        if tokens[idx].type in ['T_Comment', 'T_Whitespace']:
            tokens.pop(idx)
    return tokens

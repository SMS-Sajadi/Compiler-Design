"""
    Here we will have the Base Parts of Parser.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from lexical_analyzer.token_base import Token
from treelib import Node, Tree


def parse(tokens: List[Token]) -> Tree:
    """
    This is the main parsing function.
    :return:
    """
    tree = Tree()
    stack: list = ['$']
    token_idx: int = 0
    while len(stack) != 0:
        pass

    return tree

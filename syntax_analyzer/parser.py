"""
    Here we will have the Base Parts of Parser.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from syntax_analyzer.parser_table import get_table
from lexical_analyzer.token_base import Token
from syntax_analyzer.special_node import Node


def parse(tokens: List[Token]) -> Node:
    """
    This is the main parsing function.
    :return:
    """
    tree = Node('Program')
    stack: list = ['$', 'Program']
    tokens.append(Token('$'))

    token_idx: int = 0
    table = get_table()

    tree_stack = [tree]
    top_of_stack: str = stack.pop()

    while top_of_stack != '$':
        top_of_tree = tree_stack.pop()

        if top_of_stack[:2] == 'T_':
            if tokens[token_idx].type == top_of_stack:
                top_of_tree.value = tokens[token_idx].attribute
                token_idx += 1
            else:
                assert tokens[token_idx].type == top_of_stack, f'{top_of_stack} is not in the table!'
        else:
            body = table[top_of_stack][tokens[token_idx].type].copy()
            temp = []
            for _ in body:
                node = Node(_, parent=top_of_tree)
                temp.append(node)

            for _ in range(len(body) - 1, -1, -1):
                if body[_] == 'epsilon':
                    body.pop(_)
                    temp.pop(_)

            stack.extend(reversed(body))
            tree_stack.extend(reversed(temp))

        top_of_stack: str = stack.pop()

    return tree

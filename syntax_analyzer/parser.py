"""
    Here we will have the Base Parts of Parser.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from syntax_analyzer.parser_table import get_table
from lexical_analyzer.token_base import Token
from treelib import Tree
from anytree import Node


def parse(tokens: List[Token]) -> Node:
    """
    This is the main parsing function.
    :return:
    """
    tree = Tree()
    tree.create_node('Program', 0)
    tree2 = Node('Program')
    stack: list = ['$', 'Program']
    tokens.append(Token('$'))
    token_idx: int = 0
    table = get_table()
    identifier_stack: list = [0]
    tree_stack = [tree2]
    ident = 1
    top_of_stack: str = stack.pop()
    while top_of_stack != '$':
        top_of_identifier: int = identifier_stack.pop()
        top_of_tree = tree_stack.pop()
        if top_of_stack[:2] == 'T_':
            if tokens[token_idx].type == top_of_stack:
                token_idx += 1
            else:
                assert tokens[token_idx].type == top_of_stack, f'{top_of_stack} is not in the table!'
        else:
            body = table[top_of_stack][tokens[token_idx].type].copy()
            temp = []
            for _ in body:
                tree.create_node(_, ident, parent=top_of_identifier)
                temp.append(Node(_, parent=top_of_tree))
                ident += 1
            for _ in range(len(body) - 1, -1, -1):
                if body[_] == 'epsilon':
                    body.pop(_)
                    temp.pop(_)
            stack.extend(reversed(body))
            identifier_stack.extend(range(ident - 1, ident - len(body) - 1, -1))
            tree_stack.extend(reversed(temp))

        top_of_stack: str = stack.pop()

    return tree2

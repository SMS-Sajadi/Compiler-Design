"""
    Here we will have the Base Parts of Parser.
    This implementation is used for PL Language Compiler (PL) syntax analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from syntax_analyzer.parser_table import get_table
from lexical_analyzer.token_base import Token
from syntax_analyzer.special_node import Node
from syntax_analyzer.AutoParserTableCreator.grammar_loader import get_auto_table
from syntax_analyzer.error_handlers import (raise_error_empty_table, raise_error_synch, raise_error_suggest,
                                            raise_error_end)

from deepdiff import DeepDiff


def parse(tokens: List[Token]) -> Node:
    """
    This is the main parsing function.
    :return:
    """
    tree = Node('Program')
    stack: list = ['$', 'Program']
    tokens.append(Token('$', token_line=tokens[-1].line + 1, token_inline_index=0))

    token_idx: int = 0
    # table = get_table()
    table = get_auto_table()

    tree_stack = ['$', tree]
    top_of_stack: str = stack.pop()
    top_of_tree = tree_stack.pop()
    is_error_seen: bool = False

    exceptions: List[Exception] = []

    while top_of_stack != '$':

        if top_of_stack[:2] == 'T_':
            if tokens[token_idx].type == top_of_stack:
                top_of_tree.value = tokens[token_idx].attribute
                token_idx += 1
            else:
                is_error_seen = True
                exceptions.append(
                    raise_error_suggest(tokens[token_idx - 1], top_of_stack)
                )
        else:
            try:
                body = table[top_of_stack][tokens[token_idx].type].copy()
                if 'synch' in body:
                    is_error_seen = True
                    exceptions.append(
                        raise_error_synch(tokens, token_idx, top_of_stack)
                    )
                    top_of_stack = stack.pop()
                    continue

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
            except KeyError as e:
                is_error_seen = True
                if token_idx + 1 == len(tokens):
                    exceptions.append(
                        raise_error_end(tokens, token_idx, top_of_stack)
                    )
                    break
                exceptions.append(
                    raise_error_empty_table(tokens, token_idx, top_of_stack)
                )
                token_idx += 1
                continue

        top_of_stack: str = stack.pop()
        if not is_error_seen:
            top_of_tree = tree_stack.pop()

    if len(exceptions) != 0:
        raise ExceptionGroup(f'We have Found at least {len(exceptions)} Errors in your code:', exceptions)

    return tree

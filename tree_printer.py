"""
    This file is used for pretty printing syntax tree.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from anytree import Node, RenderTree


def print_tree(tree: Node, *, graphic_print: bool =False) -> None:
    """
    Print a tree in a pretty way.
    :param tree: The tree to be printed.
    :param graphic_print: Print graphics.
    :return:
    """
    if graphic_print:
        # TODO: fix graphic printing
        pass

    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))

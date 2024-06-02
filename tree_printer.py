"""
    This file is used for pretty printing syntax tree.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter


def print_tree(tree: Node, *, address: str, graphic_print: bool =False) -> None:
    """
    Print a tree in a pretty way.
    :param tree: The tree to be printed.
    :param address: The address of the output directory.
    :param graphic_print: Print graphics.
    :return:
    """
    if graphic_print:
        try:
            UniqueDotExporter(tree).to_picture(address + "/syntax_tree_res.png")
        except Exception as e:
            print('\033[91m' + f'You need to install graphviz and add it to your system path!')

    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))


def write_tree_to_file(tree: Node, *, address: str) -> None:
    """
    Write a tree in a pretty way to the address.
    :param tree: The tree to be printed.
    :param address: The address of the output directory.
    :return:
    """
    with open(address + '/syntax_tree.txt', 'w', encoding="utf-8") as file:
        for pre, fill, node in RenderTree(tree):
            file.write("%s%s\n" % (pre, node.name))

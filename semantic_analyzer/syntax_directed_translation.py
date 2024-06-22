"""
    Here we will have the Base Parts of Semantic Analyzer.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from syntax_analyzer.special_node import Node
from semantic_analyzer.syntax_directed_schema import add_semantic_nodes
from anytree import PostOrderIter


def check_code(syntax_tree: Node) -> None:
    """
    This function is used to check if a syntax tree is valid.
    :param syntax_tree: The syntax tree to be checked.
    :return:
    """
    add_semantic_nodes(syntax_tree)

    for node in PostOrderIter(syntax_tree):
        if node.is_semantic:
            node()

"""
    Here we will have the base structure for Grammar that the syntax analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""


class Grammar:
    """
    The Grammar class that represents each rule of the Grammar.
    """
    def __init__(self, head: str, body: list):
        self.head = head
        self.body = body

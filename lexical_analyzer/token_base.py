"""
    Here we will have the base structure for Tokens that the lexical analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""


class Token:
    """
    A Token class represents a single token in the lexical analyzer.
    """
    def __init__(self, token_type: str,
                 token_name: str = "",
                 token_attribute: str = "",
                 token_line: int = None,
                 *,
                 is_identifier=False):
        """
        Token class constructor
        :param token_type: the type of the token
        :param token_name: the name of the token
        :param token_attribute: the attribute of the token
        :param token_line: the line of token first occurrence
        :param is_identifier: it shows if attribute is whether a str or pointer to symbol table
        """
        self.type = token_type
        self.name = token_name
        self.attribute = token_attribute
        self.line = token_line
        self.is_identifier = is_identifier

    def __str__(self) -> str:
        if not self.is_identifier:
            return f"<{self.type}, {self.attribute}>"
        return f"<{self.type}, <{self.name}, {self.line}>>"

"""
    Here we will have the base structure for Tokens that the lexical analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
import codecs


class Token:
    """
    A Token class represents a single token in the lexical analyzer.
    """
    def __init__(self, token_type: str,
                 token_name: str = "",
                 token_attribute: str = "",
                 token_line: int = None,
                 token_index: int = None,
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
        # TODO: remove unnecessary attr and fix saving as repr
        self.type = token_type
        self.name = token_name
        self.attribute = token_attribute
        self.line = token_line
        self.index = token_index
        self.is_identifier = is_identifier

    def set_line(self, line_number: int):
        """
        Sets the line of the token.
        :param line_number:
        :return:
        """
        self.line = line_number

    def set_index(self, index: int):
        """
        Sets the line of the token.
        :param index:
        :return:
        """
        self.index = index

    def __str__(self) -> str:
        return f"""{self.index}: {self.name if self.type != "T_Whitespace" else "whitespace"} -> {self.type}"""

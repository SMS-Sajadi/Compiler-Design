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
                 token_attribute: str = "",
                 token_line: int = None,
                 token_index: int = None,
                 token_inline_index: int = None,
                 *,
                 is_identifier=False):
        """
        Token class constructor
        :param token_type: the type of the token
        :param token_attribute: the attribute of the token
        :param token_line: the line of token first occurrence
        :param token_index: the index of the token
        :param token_inline_index: the inline index of the token
        :param is_identifier: it shows if attribute is whether a str or pointer to symbol table
        """
        self.type = token_type
        self.attribute = token_attribute
        self.line = token_line
        self.index = token_index
        self.inline_index = token_inline_index
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

    def set_inline_index(self, inline_index: int):
        """
        Sets the inline index of the token.
        :param inline_index:
        :return:
        """
        self.inline_index = inline_index

    def __str__(self) -> str:
        return f"""{self.index}: {self.attribute if self.type != "T_Whitespace" else "whitespace"} -> {self.type}"""

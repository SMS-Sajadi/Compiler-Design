"""
    In this file, there are several functions for detecting lexemes in an entry text.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import Tuple
from token_base import Token


def is_bool(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a bool Keyword.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0:4] == "bool":
        return 4, Token("T_Bool", "bool")
    return 0, None
    # forward = 0
    # state = 0
    # while True:
    #     match state:
    #         case 0:
    #             if string[forward] != 'b':
    #                 return 0, None
    #             state = 1
    #             forward += 1
    #         case 1:
    #             if string[forward] != 'o':
    #                 return 0, None
    #             state = 2
    #             forward += 1
    #         case 2:
    #             if string[forward] != 'o':
    #                 return 0, None
    #             state = 3
    #             forward += 1
    #         case 3:
    #             if string[forward] != 'l':
    #                 return 0, None
    #             state = 4
    #         case 4:
    #             return forward, Token("T_Bool", "bool")


def is_break(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a break Keyword.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0:5] == "break":
        return 5, Token("T_Break", "break")
    return 0, None


def is_char(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a char Keyword.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0:4] == "char":
        return 4, Token("T_Char", "char")
    return 0, None


def is_comment(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a comment.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while True:
        match state:
            case 0:
                if string[forward] != '/':
                    break
                state = 1
                forward += 1
            case 1:
                if string[forward] != '/':
                    break
                state = 2
                forward += 1
            case 2:
                if string[forward] != '\n':
                    forward += 1
                else:
                    state = 3
            case 3:
                return forward, Token("T_Comment", f"{string[:forward]}")

    return 0, None


def is_whitespace(string: str) -> Tuple[bool, Token] | Tuple[bool, None]:
    """
    Check if a string is a whitespace.
    :param string: this is the entry text to be checked.
    :return: The first element is True if a '\n' character is detected and second element is the Token object.
    """
    if string[0] == '\n':
        return True, Token("T_Whitespace", "\n")
    if string[0] == '\t':
        return False, Token("T_Whitespace", "\t")
    if string[0] == ' ':
        return False, Token("T_Whitespace", " ")

    return False, None


def is_id(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a variable name or function name.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while True:
        match state:
            case 0:
                if not string[forward].isalpha() and string[forward] != '_':
                    break
                state = 1
                forward += 1
            case 1:
                if not string[forward].isalpha() and string[forward] != '_' and not string[forward].isdigit():
                    state = 2
                else:
                    forward += 1
            case 2:
                return forward, Token("T_Id", f"{string[:forward + 1]}")

    return 0, None

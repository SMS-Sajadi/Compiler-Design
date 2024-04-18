"""
    In this file, there are several functions for detecting lexemes in an entry text.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import Tuple
from token_base import Token

KEYWORDS = ['bool', 'break', 'char', 'continue', 'else', 'false', 'for', 'if', 'int', 'print', 'return', 'true']


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
    while forward < len(string):
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
                    forward += 1
            case 3:
                return forward, Token("T_Comment", f"{string[:forward]}")

    return 0, None


def is_whitespace(string: str) -> Tuple[bool, bool, Token] | Tuple[bool, bool, None]:
    """
    Check if a string is a whitespace.
    :param string: this is the entry text to be checked.
    :return: The first element is True if a '\n' character is detected and second element is True when we have
     just a tab character. The last item is the Token object.
    """
    if string[0] == '\n':
        return True, False, Token("T_Whitespace", "\\n")
    if string[:3] == '\\t':
        return False, True, Token("T_Whitespace", "\\t")
    if string[0] == ' ':
        return False, False, Token("T_Whitespace", " ")

    return False, False, None


def is_id(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a variable name or function name.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while forward < len(string):
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
                # TODO: Remove these codes
                # if string[:forward] in KEYWORDS:
                #     break
                return forward, Token("T_Id", f"{string[:forward + 1]}")

    return 0, None


def is_decimal(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a decimal number.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while forward < len(string):
        match state:
            case 0:
                if string[forward].isdigit():
                    state = 1
                    forward += 1
                    continue

                if string[forward] == '-':
                    state = 2
                    forward += 1
                    continue

                break
            case 1:
                if not string[forward].isdigit():
                    state = 3
                else:
                    forward += 1
            case 2:
                if not string[forward].isdigit():
                    break
                state = 1
                forward += 1
            case 3:
                return forward, Token("T_Decimal", f"{string[:forward]}")

    return 0, None


def is_hex(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a hexadecimal number.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while forward < len(string):
        match state:
            case 0:
                if string[forward] != '0':
                    break
                state = 1
                forward += 1
            case 1:
                if string[forward] != 'x':
                    break
                state = 2
                forward += 1
            case 2:
                if (not string[forward].isdigit()
                        and not ('A' <= string[forward] <= 'F')
                        and not ('a' <= string[forward] <= 'f')):
                    break
                state = 3
                forward += 1
            case 3:
                if (not string[forward].isdigit()
                        and not ('A' <= string[forward] <= 'F')
                        and not ('a' <= string[forward] <= 'f')):
                    state = 4
                else:
                    forward += 1
            case 4:
                return forward, Token("T_Hexadecimal", f"{string[:forward]}")

    return 0, None


def is_string(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is in-fact a string in program!
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while forward < len(string):
        match state:
            case 0:
                if string[forward] != '\"':
                    break
                state = 1
                forward += 1
            case 1:
                if string[forward:forward + 2] == r"\"":
                    forward += 2
                elif string[forward] != '\"':
                    forward += 1
                else:
                    forward += 1
                    state = 3
            # case 2:
            #     if string[forward] not in ['\"', '\'', '\n', '\t', '\b', '\a', '\\']:
            #         break
            #     state = 1
            #     forward += 1
            case 3:
                return forward, Token("T_String", f"{string[:forward]}")

    return 0, None


def is_character(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a character.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while forward < len(string):
        match state:
            case 0:
                if string[forward] != '\'':
                    break
                state = 1
                forward += 1
            case 1:
                if string[forward:forward + 2] == r"\'" or string[forward:forward + 2] == r'\\':
                    forward += 2
                    state = 3
                    continue

                state = 3
                forward += 1
            case 3:
                if string[forward] != '\'':
                    break
                state = 4
                forward += 1
            case 4:
                return forward, Token("T_Character", f"{string[:forward]}")

    return 0, None


def is_delimiter(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a delimiter character.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0] == ',':
        return 1, Token("T_Comma", f"{string[0]}")

    if string[0] == ';':
        return 1, Token("T_Semicolon", f"{string[0]}")

    return 0, None


def is_bracket(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a bracket character.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0] == ']':
        return 1, Token("T_RB", f"{string[0]}")

    if string[0] == '[':
        return 1, Token("T_LB", f"{string[0]}")

    return 0, None


def is_curly_bracket(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a curly bracket character.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0] == '}':
        return 1, Token("T_RC", f"{string[0]}")

    if string[0] == '{':
        return 1, Token("T_LC", f"{string[0]}")

    return 0, None


def is_parenthesis(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a Parenthesis character.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0] == ')':
        return 1, Token("T_RP", f"{string[0]}")

    if string[0] == '(':
        return 1, Token("T_LP", f"{string[0]}")

    return 0, None


def is_assignment(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is an assignment character.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0] == '=':
        return 1, Token("T_Assign", f"{string[0]}")

    return 0, None


def is_logical(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string has a logical token.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[:2] == "&&":
        return 2, Token("T_LOp_AND", f"{string[:2]}")

    if string[:2] == "||":
        return 2, Token("T_LOp_OR", f"{string[:2]}")

    if string[0] == '!':
        return 1, Token("T_LOp_NOT", f"{string[0]}")

    return 0, None

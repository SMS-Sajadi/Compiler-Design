"""
    In this file, there are several functions for detecting lexemes in an entry text.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import Tuple, Final
from lexical_analyzer.token_base import Token

KEYWORDS: Final = ['bool', 'break', 'char', 'continue', 'else', 'false', 'for', 'if', 'int', 'print', 'return', 'true']
DIGITS: Final = "0123456789"
ALPHA: Final = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_bool(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a bool Keyword.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0:4] == "bool":
        return 4, Token("T_Bool", "bool")
    return 0, None


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


def is_continue(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a continue Keyword.
    :param string:
    :return:
    """
    if string[:8] == "continue":
        return 8, Token("T_Continue", "continue")
    return 0, None


def is_else(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is an else Keyword.
    :param string:
    :return:
    """
    if string[:4] == "else":
        return 4, Token("T_Else", "else")
    return 0, None


def is_false(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a false Keyword.
    :param string:
    :return:
    """
    if string[:5] == "false":
        return 5, Token("T_False", "false")
    return 0, None


def is_for(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a for Keyword.
    :param string:
    :return:
    """
    if string[:3] == "for":
        return 3, Token("T_For", "for")
    return 0, None


def is_if(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is an if Keyword.
    :param string:
    :return:
    """
    if string[:2] == "if":
        return 2, Token("T_If", "if")
    return 0, None


def is_int(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a int Keyword.
    :param string:
    :return:
    """
    if string[:3] == "int":
        return 3, Token("T_Int", "int")
    return 0, None


def is_print(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a print Keyword.
    :param string:
    :return:
    """
    if string[:5] == "print":
        return 5, Token("T_Print", "print")
    return 0, None


def is_return(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a return Keyword.
    :param string:
    :return:
    """
    if string[:6] == "return":
        return 6, Token("T_Return", "return")
    return 0, None


def is_true(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if a string is a true Keyword.
    :param string:
    :return:
    """
    if string[:4] == "true":
        return 4, Token("T_True", "true")
    return 0, None


def is_comment(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a comment.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while state == 3 or forward < len(string):
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
                return forward, Token("T_Comment", f"{string[:forward - 1]}")

    return 0, None


def is_whitespace(string: str) -> Tuple[int, int, Token] | Tuple[int, int, None]:
    """
    Check if entry string is whitespace token.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of ws token that is detected and second element is number of newline
     characters that are seen in the token. The last item is the Token object itself.
    """
    forward = 0
    new_line = 0
    while forward < len(string):
        if string[forward] == '\n':
            new_line += 1
            forward += 1

        elif string[forward] == ' ' or string[forward] == '\t':
            forward += 1

        else:
            break

    if forward == 0:
        return 0, 0, None

    return forward, new_line, Token("T_Whitespace", f"{repr(string[:forward])}")


def is_id(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a variable name or function name.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while state == 2 or forward < len(string):
        match state:
            case 0:
                if not string[forward].isalpha() and string[forward] != '_':  # OR not string[forward] in ALPHA
                    break
                state = 1
                forward += 1
            case 1:
                if not string[forward].isalpha() and string[forward] != '_' and not string[forward].isdigit():
                    state = 2
                else:
                    forward += 1

            case 2:
                return forward, Token("T_Id", f"{string[:forward]}")

        if forward == len(string):
            state = 2

    return 0, None


def is_decimal(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a decimal number.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while state == 2 or forward < len(string):
        match state:
            case 0:
                if string[forward].isdigit():
                    state = 1
                    forward += 1
                    continue

                break
            case 1:
                if not string[forward].isdigit():
                    state = 2
                else:
                    forward += 1

                if forward == len(string):
                    state = 2
            case 2:
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
    while state == 4 or forward < len(string):
        match state:
            case 0:
                if string[forward] != '0':
                    break
                state = 1
                forward += 1
            case 1:
                if string[forward] != 'x' and string[forward] != 'X':
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

                if forward == len(string):
                    state = 4

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
    while state == 2 or forward < len(string):
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
                    state = 2
            case 2:
                return forward, Token("T_String", fr"{string[:forward]}")

    return 0, None


def is_character(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string is a character.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while state == 4 or forward < len(string):
        match state:
            case 0:
                if string[forward] != '\'':
                    break
                state = 1
                forward += 1
            case 1:
                if string[forward:forward + 2] == r"\'":
                    forward += 2
                    state = 3
                    continue

                if string[forward] == '\\':
                    forward += 1
                    state = 2
                    continue

                elif string[forward] != '\'':
                    state = 3
                    forward += 1
                    continue

                break
            case 2:
                if string[forward] == '\'':
                    break
                state = 3
                forward += 1
            case 3:
                if string[forward] != '\'':
                    break
                state = 4
                forward += 1
            case 4:
                return forward, Token("T_Character", fr"{string[:forward]}")

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


def is_relational(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string has a relational token.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    forward = 0
    state = 0
    while forward < len(string):
        match state:
            case 0:
                if string[forward] == '<':
                    forward += 1
                    state = 1
                    continue

                if string[forward] == '>':
                    forward += 1
                    state = 2
                    continue

                if string[forward] == '!':
                    forward += 1
                    state = 3
                    continue

                if string[forward] == '=':
                    forward += 1
                    state = 4
                    continue

                break

            case 1:
                if string[forward] == '=':
                    forward += 1
                    return forward, Token("T_ROp_LE", f"{string[:forward]}")
                else:
                    return forward, Token("T_ROp_L", f"{string[:forward]}")

            case 2:
                if string[forward] == '=':
                    forward += 1
                    return forward, Token("T_ROp_GE", f"{string[:forward]}")
                else:
                    return forward, Token("T_ROp_G", f"{string[:forward]}")

            case 3:
                if string[forward] == '=':
                    forward += 1
                    return forward, Token("T_ROp_NE", f"{string[:forward]}")
                else:
                    break

            case 4:
                if string[forward] == '=':
                    forward += 1
                    return forward, Token("T_ROp_E", f"{string[:forward]}")
                else:
                    break

    if state == 1 and forward == len(string):
        return forward, Token("T_ROp_L", f"{string[:forward]}")

    if state == 2 and forward == len(string):
        return forward, Token("T_ROp_G", f"{string[:forward]}")

    return 0, None


def is_arithmatic(string: str) -> Tuple[int, Token] | Tuple[int, None]:
    """
    Check if the string has an arithmatic token.
    :param string: this is the entry text to be checked.
    :return: The first element is the length of detected token and second element is the Token object.
    """
    if string[0] == '+':
        return 1, Token("T_AOp_PL", f"{string[0]}")

    if string[0] == '-':
        return 1, Token("T_AOp_MN", f"{string[0]}")

    if string[0] == '*':
        return 1, Token("T_AOp_ML", f"{string[0]}")

    if string[0] == '/':
        return 1, Token("T_AOp_DV", f"{string[0]}")

    if string[0] == '%':
        return 1, Token("T_AOp_RM", f"{string[0]}")

    return 0, None

"""
    Here we will have the base structure for Error handler in PL syntax analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from lexical_analyzer.token_base import Token
from typing import List


def raise_error_empty_table(tokens: List[Token], token_idx: int, top_of_stack: str) -> SyntaxError:
    """
    This function will create proper error base on token and stack when there was no key in table!
    :param token: The token that error occurs by
    :param top_of_stack: The Part we are looking for
    :return:
    """
    token = tokens[token_idx]
    code_line = PROGRAM.splitlines()[token.line - 1]

    exception = SyntaxError(f"Error Found in line {token.line - 1}, We Found Nothing in the table to match\n"
                             f"{code_line}\n"
                             f"{' ' * (token.inline_index + len(tokens[token_idx - 1].attribute) + 1)}^~~~~~~~~~~\n"
                             f"We Suggests To Use {top_of_stack} instead of {token.attribute}")
    return exception


def raise_error_synch(tokens: List[Token], token_idx: int, top_of_stack: str) -> SyntaxError:
    """
    This function will create proper error base on token and stack when there was no key in table!
    :param token: The token that error occurs by
    :param top_of_stack: The Part we are looking for
    :return:
    """
    token = tokens[token_idx - 1]
    code_line = PROGRAM.splitlines()[token.line - 1]

    exception = SyntaxError(f"Error Found in line {token.line}, We Found Synch in the table\n"
                             f"{code_line}\n"
                             f"{' ' * (token.inline_index + len(tokens[token_idx].attribute) + 1)}^~~~~~~~~~~\n")
    return exception


def raise_error_end(tokens: List[Token], token_idx: int, top_of_stack: str) -> SyntaxError:
    """
    This function will create proper error base on token and stack when there was no key in table!
    :param token: The token that error occurs by
    :param top_of_stack: The Part we are looking for
    :return:
    """
    token = tokens[token_idx - 1]
    code_line = PROGRAM.splitlines()[token.line - 1]

    exception = SyntaxError(f"Error Found in line {token.line}\n"
                            f"{code_line}\n"
                            f"{' ' * (token.inline_index + len(tokens[token_idx - 1].attribute) + 1)}^~~~~~~~~~~\n"
                            f"You May Forgotten to close the curly-bracket!")
    return exception


def raise_error_suggest(token: Token, top_of_stack: str) -> SyntaxError:
    """
    This function will create proper error base on token and stack when there was no key in table!
    :param token: The token that error occurs by
    :param top_of_stack: The Part we are looking for
    :return:
    """
    code_line = PROGRAM.splitlines()[token.line - 1]

    exception = SyntaxError(f"Error Found in line {token.line - 1}\n"
                             f"{code_line}\n"
                             f"{' ' * (token.inline_index + 1)}^~~~~~~~~~~\n"
                             f"We Suggests To Use {top_of_stack}")
    return exception

def set_program(program: str) -> None:
    """
    This function will set the Program for using by error handler
    :param program: The Source code
    :return:
    """
    global PROGRAM
    PROGRAM = program
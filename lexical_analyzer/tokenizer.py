"""
    In this file, there is a function which implements the lexical analyzer for the PL Language.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from lexical_analyzer.token_base import Token
from lexical_analyzer import lexeme_detectors as ld
import sys


def tokenize(program: str) -> List[Token]:
    """
    Tokenize a program into a list of tokens.
    :param program: The program source code.
    :return: List of tokens.
    """
    tokens: List[Token] = []

    # TODO: Set to 0
    lexeme_begin: int = 0
    line: int = 1
    inline_index: int = 0
    while lexeme_begin < len(program):
        max_forward: int = 0  # TODO: set it to 0
        final_token: Token | None = None

        forward, new_lines, token = ld.is_whitespace(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_bool(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_break(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_char(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_continue(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_return(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_if(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_else(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_for(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_false(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_true(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_int(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_print(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_comment(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token
            new_lines = 1

        forward, token = ld.is_string(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_character(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_delimiter(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_bracket(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_curly_bracket(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_parenthesis(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_assignment(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_logical(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_relational(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_arithmatic(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_decimal(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_hex(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_id(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        try:
            final_token.set_index(lexeme_begin)
            final_token.set_inline_index(inline_index)
            lexeme_begin += max_forward
            inline_index += max_forward
            final_token.set_line(line)
            line += new_lines
            if new_lines != 0:
                inline_index = 0
            tokens.append(final_token)
        except AttributeError as error:
            code_line = program.splitlines()[line-1]

            print('\033[91m'+f"Token Not Found!\n"
                          f"Lexical Analyzer Error in:\n"
                          f"{line}:{code_line}")
            print('\033[91m'+f"{' '* (inline_index + len(str(line)) + 1)}^~~~~~~~~~~")
            sys.exit(-1)

    return tokens

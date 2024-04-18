"""
    In this file, there is a function which implements the lexical analyzer for the PL Language.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from token_base import Token
import lexeme_detectors as ld


def tokenize(program: str) -> List[Token]:
    tokens: List[Token] = []

    lexeme_begin: int = 0
    line: int = 1
    while lexeme_begin < len(program):
        is_new_line, is_tab, whitespace_token = ld.is_whitespace(program[lexeme_begin:])
        if whitespace_token is not None:
            if is_tab:
                lexeme_begin += 2
            else:
                lexeme_begin += 1
            tokens.append(whitespace_token)
            if is_new_line:
                line += 1
            continue

        forward, token = ld.is_bool(program[lexeme_begin:])
        if token is not None:
            tokens.append(token)
            lexeme_begin += forward
            continue

        forward, token = ld.is_break(program[lexeme_begin:])
        if token is not None:
            tokens.append(token)
            lexeme_begin += forward
            continue

        forward, token = ld.is_char(program[lexeme_begin:])
        if token is not None:
            tokens.append(token)
            lexeme_begin += forward
            continue

        forward, token = ld.is_comment(program[lexeme_begin:])
        if token is not None:
            tokens.append(token)
            lexeme_begin += forward
            continue

        forward, token = ld.is_string(program[lexeme_begin:])
        if token is not None:
            tokens.append(token)
            lexeme_begin += forward
            continue

        forward, token = ld.is_character(program[lexeme_begin:])
        if token is not None:
            tokens.append(token)
            lexeme_begin += forward
            continue

        forward, token = ld.is_id(program[lexeme_begin:])
        if token is not None:
            tokens.append(token)
            lexeme_begin += forward
            continue

        lexeme_begin += 1

        # detected_tokens: List[Tuple[int, Token | None]] = list()

        # detected_tokens.append(ld.is_bool(program[lexeme_begin:]))
        # detected_tokens.append(ld.is_break(program[lexeme_begin:]))
        # detected_tokens.append(ld.is_char(program[lexeme_begin:]))
        # detected_tokens.append(ld.is_comment(program[lexeme_begin:]))
        # detected_tokens.append(ld.is_id(program[lexeme_begin:]))

        # max_forward = max(detected_tokens, key=lambda x: x[1])
        # for forward, token in detected_tokens:
        #     if forward == max_forward:


    # for line, code in enumerate(program.splitlines(keepends=True), start=1):
    #
    #     for token in code.split():
    #         pass

    return tokens


print(*tokenize(r"""
"\"helllo"
int main() {
// helsd;fks;dk;sldkf
    bool x = true;
    return 0;
}"""))

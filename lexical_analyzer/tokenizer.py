"""
    In this file, there is a function which implements the lexical analyzer for the PL Language.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from token_base import Token
import lexeme_detectors as ld


KEYWORDS = ['bool', 'break', 'char', 'continue', 'else', 'false', 'for', 'if', 'int', 'print', 'return', 'true']


def tokenize(program: str) -> List[Token]:
    tokens: List[Token] = []

    lexeme_begin = 0
    while lexeme_begin < len(program):
        temp = ld.is_bool(program[lexeme_begin:])
        temp = ld.is_break(program[lexeme_begin:])
        lexeme_begin += 1

    # for line, code in enumerate(program.splitlines(keepends=True), start=1):
    #
    #     for token in code.split():
    #         pass

    return tokens


tokenize("""
int main() {
    bool x = true;
    return 0;
}""")

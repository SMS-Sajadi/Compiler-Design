"""
    Here we will have the base structure for Error handler in PL semantic analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""


def raise_error(msg: str, line: int, inline_index: int) -> SystemError:
    code_line = PROGRAM.splitlines()[line - 1].strip()

    exception = SystemError(f"Error Found in line {line}, {msg}\n"
                             f"{code_line}\n"
                             f"{' ' * (inline_index)}^~~~~~~~~~~\n")
    raise exception


def raise_no_main_error(msg: str) -> SystemError:
    exception = SystemError(msg)
    raise exception


def set_program_for_semantic_error(program: str) -> None:
    """
    This function will set the Program for using by error handler
    :param program: The Source code
    :return:
    """
    global PROGRAM
    PROGRAM = program

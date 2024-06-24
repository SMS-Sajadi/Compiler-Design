"""
    Here we have the basic function table and variable declarations table.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""


class Function:
    def __init__(self, name):
        self.name = name
        self.entries = []
        self.return_type = None
        self.has_return = False
        self.declaration_line = 0
        self.declaration_inline_index = 0


class Variable:
    def __init__(self, name):
        self.name = name
        self.ctype = None
        self.scope_start = -1
        self.scope_end = -1
        self.scope = -1

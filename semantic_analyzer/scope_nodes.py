"""
    Here we will have the base structure for Scope that the semantic analyzer uses.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from anytree import NodeMixin


class Scope(NodeMixin):
    def __init__(self, name, value='', parent=None, children=None):
        super().__init__()
        self.name = name
        self.value = value
        self.parent = parent
        if children:
            self.children = children

    def __str__(self):
        return self.name

"""
    Here we will have the base structure for Node that the syntax analyzer uses to create tree.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from anytree import NodeMixin


class Node(NodeMixin):  # Add Node feature
    def __init__(self, name, value='', parent=None, children=None, is_semantic=False, func=None):
        super(Node, self).__init__()
        self.name = name
        self.value = value
        self.parent = parent
        self.is_semantic = is_semantic
        self.run = func
        self.ctype = None
        self.base_type = None
        self.line = 0
        self.inline_index = 0
        if children:  # set children only if given
            self.children = children

    def __str__(self):
        return self.name

    def __call__(self):
        self.run(self)


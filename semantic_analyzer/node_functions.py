"""
    Here we have all functions that are needed for semantic nodes.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from semantic_analyzer.basic_classes import Function
from syntax_analyzer.special_node import Node

FUNCTIONS: List[Function] = []


def add_function(self: Node):
    function_name = self.siblings[0].func_name

    for func in FUNCTIONS:
        if func.name == function_name:
            raise Exception("Function already exists")

    new_function = Function(function_name)
    FUNCTIONS.append(new_function)


def set_function_attributes(self: Node):
    self.parent.func_name = self.siblings[1].value


def check_main(self: Node):
    for func in FUNCTIONS:
        if func.name == 'main':
            break
    else:
        raise Exception("No main function")

"""
    Here we have all functions that are needed for semantic nodes.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from semantic_analyzer.basic_classes import Function, Variable
from syntax_analyzer.special_node import Node

FUNCTIONS: List[Function] = []
VARIABLES: List[Variable] = []


def add_function(self: Node):
    function_name = self.siblings[0].func_name
    function_return_type = self.siblings[0].ctype

    for func in FUNCTIONS:
        if func.name == function_name:
            raise Exception("Function already exists")

    new_function = Function(function_name)
    new_function.return_type = function_return_type
    FUNCTIONS.append(new_function)


def set_function_attributes(self: Node):
    self.parent.func_name = self.siblings[1].value
    self.parent.ctype = self.siblings[0].ctype


def check_main(self: Node):
    for func in FUNCTIONS:
        if func.name == 'main':
            if func.return_type != 'int':
                raise Exception("Main Function Return Type should be int!")
            break
    else:
        raise Exception("No main function")


def set_type(self: Node):
    self.parent.ctype = self.siblings[0].value


def set_declaration_expected_type(self: Node):
    self.siblings[1].base_type = self.siblings[0].ctype


def set_var_declaration_expected_type(self: Node):
    for node in self.siblings:
        node.base_type = self.parent.base_type


def set_bracket_type(self: Node):
    self.parent.ctype = f"array({self.siblings[1].value}, {self.siblings[3].ctype})"
    self.base_type = self.parent.base_type


def set_bracket_type_end(self: Node):
    self.parent.ctype = self.parent.base_type


def set_bracket_base_type(self: Node):
    self.siblings[1].base_type = self.parent.base_type


def set_declaration_var(self: Node):
    self.parent.var_name = self.siblings[0].value
    self.parent.ctype = self.siblings[-1].ctype


def set_declaration_assign(self: Node):
    if len(self.siblings) != 1:
        self.parent.ctype = self.siblings[-1].ctype
    else:
        self.parent.ctype = "epsilon"


def add_variable(self: Node):
    var_name = self.siblings[1].var_name
    var_type = self.siblings[1].ctype

    for var in VARIABLES:
        if var.name == var_name:
            raise Exception("Variable already exists")

    new_var = Variable(var_name)
    new_var.ctype = var_type
    # TODO: Add type check
    VARIABLES.append(new_var)



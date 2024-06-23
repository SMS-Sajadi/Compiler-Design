"""
    Here we have all functions that are needed for semantic nodes.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from semantic_analyzer.basic_classes import Function, Variable
from syntax_analyzer.special_node import Node
from semantic_analyzer.error_handlers import raise_error

FUNCTIONS: List[Function] = []
VARIABLES: List[Variable] = []


def add_function(self: Node):
    function_name = self.siblings[0].func_name
    function_return_type = self.siblings[0].ctype
    line = self.siblings[0].line
    inline_index = self.siblings[0].inline_index

    for func in FUNCTIONS:
        if func.name == function_name:
            raise_error("Function already exists", line, inline_index)

    new_function = Function(function_name)
    new_function.return_type = function_return_type
    FUNCTIONS.append(new_function)


def add_variable(self: Node):
    var_name = self.siblings[1].var_name
    var_type = self.siblings[1].ctype
    line = self.siblings[1].line
    inline_index = self.siblings[1].inline_index

    for var in VARIABLES:
        if var.name == var_name:
            raise_error("Variable already exists", line, inline_index)

    new_var = Variable(var_name)
    new_var.ctype = var_type
    # TODO: Add type check
    VARIABLES.append(new_var)


def set_function_attributes(self: Node):
    self.parent.func_name = self.siblings[1].value
    self.parent.ctype = self.siblings[0].ctype
    self.parent.line = self.siblings[1].line
    self.parent.inline_index = self.siblings[1].inline_index


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
    self.parent.line = self.siblings[0].line
    self.parent.inline_index = self.siblings[0].inline_index


def set_declaration_expected_type(self: Node):
    self.siblings[1].base_type = self.siblings[0].ctype


def set_var_declaration_expected_type(self: Node):
    for node in self.siblings:
        node.base_type = self.parent.base_type


def set_bracket_type(self: Node):
    line = self.siblings[1].line
    inline_index = self.siblings[1].inline_index

    if self.siblings[1].ctype != "int":
        raise_error("You Should use integer in the bracket", line, inline_index)

    self.parent.ctype = f"array({self.siblings[1].value}, {self.siblings[4].ctype})"
    self.parent.line = self.siblings[4].line
    self.parent.inline_index = self.siblings[4].inline_index


def set_bracket_type_end(self: Node):
    self.parent.ctype = self.parent.base_type


def set_bracket_base_type(self: Node):
    self.siblings[-2].base_type = self.parent.base_type


def set_declaration_var(self: Node):
    self.parent.var_name = self.siblings[0].value
    self.parent.ctype = self.siblings[-1].ctype
    self.parent.line = self.siblings[0].line
    self.parent.inline_index = self.siblings[0].inline_index


def set_declaration_assign(self: Node):
    if len(self.siblings) != 1:
        self.parent.ctype = self.siblings[-1].ctype
    else:
        self.parent.ctype = "epsilon"


def set_const_value(self: Node):
    self.parent.value = self.siblings[0].value
    self.parent.ctype = self.siblings[0].ctype
    self.parent.line = self.siblings[0].line
    self.parent.inline_index = self.siblings[0].inline_index


def set_immutable_type_numeric(self: Node):
    self.parent.ctype = self.siblings[1].ctype
    self.parent.line = self.siblings[1].line
    self.parent.inline_index = self.siblings[1].inline_index


def set_immutable_type_relational(self: Node):
    self.parent.ctype = self.siblings[1].ctype
    self.parent.line = self.siblings[1].line
    self.parent.inline_index = self.siblings[1].inline_index


def give_type_to_next_numeric(self: Node):
    if len(self.siblings) == 3:
        self.siblings[1].base_type = self.siblings[0].ctype
        self.siblings[1].line = self.siblings[0].line
        self.siblings[1].inline_index = self.siblings[0].inline_index
    else:
        line = self.siblings[1].line
        inline_index = self.siblings[1].inline_index

        if self.siblings[1].ctype != "int":
            raise_error("You can't Use non numeric values!", line, inline_index)

        self.siblings[2].base_type = self.siblings[1].ctype
        self.siblings[2].line = self.siblings[1].line
        self.siblings[2].inline_index = self.siblings[1].inline_index


def give_type_to_next_relational(self: Node):
    if len(self.siblings) == 3:
        self.siblings[1].base_type = self.siblings[0].ctype
        self.siblings[1].line = self.siblings[0].line
        self.siblings[1].inline_index = self.siblings[0].inline_index
    else:
        line = self.siblings[1].line
        inline_index = self.siblings[1].inline_index

        if self.siblings[1].ctype != self.parent.base_type:
            raise_error("When You are Comparing, both sides should have the same type!", line, inline_index)

        self.siblings[2].base_type = self.siblings[1].ctype
        self.siblings[2].line = self.siblings[1].line
        self.siblings[2].inline_index = self.siblings[1].inline_index


def give_type_to_next_logical(self: Node):
    if len(self.siblings) == 3:
        self.siblings[1].base_type = self.siblings[0].ctype
        self.siblings[1].line = self.siblings[0].line
        self.siblings[1].inline_index = self.siblings[0].inline_index
    else:
        line = self.parent.line
        inline_index = self.parent.inline_index

        if self.parent.base_type != "bool":
            raise_error("You must use a logical expression!", line, inline_index)

        line = self.siblings[1].line
        inline_index = self.siblings[1].inline_index

        if self.siblings[1].ctype != "bool":
            raise_error("You must use a logical expression!", line, inline_index)

        self.siblings[2].base_type = self.siblings[1].ctype
        self.siblings[2].line = self.siblings[1].line
        self.siblings[2].inline_index = self.siblings[1].inline_index


def give_type_to_parent_end(self: Node):
    self.parent.ctype = self.parent.base_type


def give_type_to_parent(self: Node):
    self.parent.ctype = self.siblings[-1].ctype
    self.parent.line = self.siblings[-1].line
    self.parent.inline_index = self.siblings[-1].inline_index


def give_type_to_parent_relational(self: Node):
    self.parent.ctype = "bool"
    self.parent.line = self.siblings[-1].line
    self.parent.inline_index = self.siblings[-1].inline_index

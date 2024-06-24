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
    new_function.entries = self.siblings[0].parameters
    FUNCTIONS.append(new_function)


def add_variable(self: Node):
    var_name = self.siblings[1].var_name
    var_type = self.siblings[1].ctype
    line = self.siblings[1].line
    inline_index = self.siblings[1].inline_index

    for var in VARIABLES:
        if var.name == var_name and var.scope_end >= line >= var.scope_start:
            raise_error(f"You have declared the variable in line {var.scope_start}", line, inline_index)

    assignment_type = self.siblings[2].ctype
    inline_index += len(var_name) + 2

    if assignment_type != var_type and assignment_type != "epsilon":
        raise_error(f"Variable type mismatch, you should assign {var_type} "
                    f"expression but assigned {assignment_type}!", line, inline_index)

    new_var = Variable(var_name)
    new_var.ctype = var_type
    new_var.scope_start = self.siblings[1].line
    new_var.scope_end = self.parent.end_scope
    VARIABLES.append(new_var)


def set_function_attributes(self: Node):
    self.parent.func_name = self.siblings[1].value
    self.parent.ctype = self.siblings[0].ctype
    self.parent.line = self.siblings[1].line
    self.parent.inline_index = self.siblings[1].inline_index
    self.parent.parameters = self.siblings[4].parameters


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
    self.siblings[1].start_scope = self.parent.start_scope
    self.siblings[1].end_scope = self.parent.end_scope


def set_var_declaration_expected_type(self: Node):
    for node in self.siblings:
        node.base_type = self.parent.base_type
        node.start_scope = self.parent.start_scope
        node.end_scope = self.parent.end_scope


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
        self.parent.line = self.siblings[-1].line
        self.parent.inline_index = self.siblings[-1].inline_index
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


def give_func_return_type_to_stmts(self: Node):
    self.siblings[7].func_return_type = self.siblings[0].ctype
    self.siblings[7].start_scope = self.siblings[6].line
    self.siblings[7].end_scope = self.siblings[8].line


def give_func_return_type(self: Node):
    for node in self.siblings:
        node.func_return_type = self.parent.func_return_type
        node.start_scope = self.parent.start_scope
        node.end_scope = self.parent.end_scope


def set_return_state(self: Node):
    func_return_type = self.parent.func_return_type
    return_expr_type = self.siblings[1].ctype
    line = self.siblings[1].line
    inline_index = self.siblings[1].inline_index

    if func_return_type != return_expr_type:
        raise_error(f"Function Return Type is {func_return_type}, but you have returned {return_expr_type}!",
                    line, inline_index)


def check_assignment_state(self: Node):
    expected_type = self.parent.expected_type
    expression_type = self.siblings[-1].ctype if len(self.siblings) > 1 else "epsilon"
    line = self.siblings[-1].line
    inline_index = self.siblings[-1].inline_index

    if len(self.siblings) == 3 and expected_type != "int":
        raise_error("You can't use arithmatic assignment for non numeric values!", line, 0)

    if expected_type != expression_type and expected_type != "epsilon":
        raise_error(f"Expected type {expected_type}, but you have assigned {expression_type}!", line, inline_index)


def set_assignment_expected_type(self: Node):
    self.siblings[0].expected_type = self.parent.expected_type


def give_base_type_to_bracket(self: Node):
    line = self.siblings[0].line
    inline_index = self.siblings[0].inline_index

    for var in VARIABLES:
        if var.name == self.siblings[0].value:
            self.siblings[1].base_type = var.ctype
            break
    else:
        raise_error("You must declare the variable first!", line, inline_index)


def set_bracket_type_inuse(self: Node):
    bracket_index_type = self.siblings[1].ctype
    line = self.siblings[1].line
    inline_index = self.siblings[1].inline_index

    if bracket_index_type != "int":
        raise_error("You must use an int expression as the bracket index!", line, inline_index)

    base_type: str = self.parent.base_type
    try:
        idx = base_type.index(',')
        new_base_type = base_type[idx + 2:-1]
        self.siblings[3].base_type = new_base_type
    except ValueError:
        raise_error(f"The type is {base_type} and you can't add any more brackets", line, inline_index)


def check_mutable_type(self: Node):
    ctype = self.siblings[-1].ctype
    line = self.siblings[0].line
    inline_index = self.siblings[0].inline_index

    if ctype != "int":
        raise_error(f"Type is {ctype} and arithmatic operations can't be done on it!", line, inline_index)


def set_bracket_type_inuse_end(self: Node):
    if len(self.siblings) == 1:
        self.parent.ctype = self.parent.base_type
    else:
        self.parent.ctype = self.siblings[-1].ctype


def set_bracket_type_in_exp(self: Node):
    line = self.siblings[0].line
    inline_index = self.siblings[0].inline_index

    self.siblings[1].line = line
    self.siblings[1].inline_index = inline_index

    has_declared = False

    for var in VARIABLES:
        if var.name == self.siblings[0].value:
            self.siblings[1].base_type = var.ctype
            has_declared = True
            break

    for func in FUNCTIONS:
        if func.name == self.siblings[0].value:
            self.siblings[1].base_type = func.return_type
            has_declared = True
            break

    if not has_declared:
        raise_error("You must declare the variable first!", line, inline_index)


def give_type_to_parent_mutable_or_function(self: Node):
    self.parent.value = self.siblings[2].value
    self.parent.ctype = self.siblings[2].ctype
    self.parent.line = self.siblings[2].line
    self.parent.inline_index = self.siblings[2].inline_index


def set_bracket_base_type_in_check_call(self: Node):
    self.siblings[0].base_type = self.parent.expected_type


def set_assignment_expected_type_for_bracket(self: Node):
    self.siblings[2].expected_type = self.siblings[1].ctype


def set_scope_for_function_params(self: Node):
    self.siblings[3].start_scope = self.siblings[5].line
    self.siblings[3].end_scope = self.siblings[8].line
    self.siblings[3].parameters = []


def give_scope_to_others(self: Node):
    for node in self.siblings:
        node.start_scope = self.parent.start_scope
        node.end_scope = self.parent.end_scope

        if self.parent.name in ["function_params", "params_list"]:
            node.parameters = self.parent.parameters


def set_bracket_base_type_in_function_def(self: Node):
    self.siblings[2].base_type = self.siblings[0].ctype


def add_parameter(self: Node):
    var_name = self.siblings[1].value
    var_type = self.siblings[3].ctype
    line = self.siblings[0].line
    inline_index = self.siblings[0].inline_index
    scope_start = self.parent.start_scope
    scope_end = self.parent.end_scope

    for var in VARIABLES:
        if var.name == var_name and var.scope_end >= line >= var.scope_start:
            raise_error(f"You have declared the variable in line {var.scope_start}", line, inline_index)

    new_var = Variable(var_name)
    new_var.ctype = var_type
    new_var.scope_start = scope_start
    new_var.scope_end = scope_end
    VARIABLES.append(new_var)
    self.parent.parameters.append(new_var)


def get_id_type(self: Node):
    id_name = self.siblings[0].value
    line = self.siblings[0].line
    inline_index = self.siblings[0].inline_index
    has_declared = False

    for variable in VARIABLES:
        if variable.name == id_name and variable.scope_end >= line >= variable.scope_start:
            self.siblings[1].expected_type = variable.ctype
            has_declared = True

    for func in FUNCTIONS:
        if func.name == id_name:
            has_declared = True
            break

    if not has_declared:
        raise_error("You must declare the variable first!", line, inline_index)

    # TODO: Prevent from creating a var with the name of a function

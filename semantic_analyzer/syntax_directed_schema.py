"""
    Here we will have the SDD for the PL language.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import Final
from syntax_analyzer.special_node import Node
from semantic_analyzer.node_functions import *
from copy import deepcopy

add_function_node = Node('add_function', is_semantic=True, func=add_function)
check_main_node = Node('check_main', is_semantic=True, func=check_main)
set_type_node = Node('set_type', is_semantic=True, func=set_type)
set_declaration_expected_type_node = Node('set_declaration_expected_type', is_semantic=True,
                                          func=set_declaration_expected_type)
set_bracket_type_node = Node('set_bracket_type', is_semantic=True, func=set_bracket_type)
set_bracket_type_end_node = Node('set_bracket_type_end', is_semantic=True, func=set_bracket_type_end)
set_bracket_base_type_node = Node('set_bracket_base_type', is_semantic=True, func=set_bracket_base_type)
set_declaration_var_node = Node('set_declaration_var', is_semantic=True, func=set_declaration_var)
set_declaration_assign_node = Node('set_declaration_assign', is_semantic=True, func=set_declaration_assign)
add_variable_node = Node('add_variable', is_semantic=True, func=add_variable)
set_var_declaration_expected_type_node = Node('set_var_declaration_expected_type', is_semantic=True,
                                              func=set_var_declaration_expected_type)
set_const_value_node = Node('set_const_value', is_semantic=True, func=set_const_value)
set_immutable_type_numeric_node = Node('set_immutable_type_numeric_node', is_semantic=True,
                                       func=set_immutable_type_numeric)
set_immutable_type_relational_node = Node('set_immutable_type_relational', is_semantic=True,
                                          func=set_immutable_type_relational)
give_type_to_next_numeric_node = Node('give_type_to_next', is_semantic=True, func=give_type_to_next_numeric)
give_type_to_parent_end_node = Node('give_type_to_parent_end', is_semantic=True, func=give_type_to_parent_end)
give_type_to_parent_node = Node('give_type_to_parent', is_semantic=True, func=give_type_to_parent)
give_type_to_next_relational_node = Node('give_type_to_next_relational', is_semantic=True,
                                         func=give_type_to_next_relational)
give_type_to_parent_relational_node = Node('give_type_to_parent_relational', is_semantic=True,
                                           func=give_type_to_parent_relational)
give_type_to_next_logical_node = Node('give_type_to_next_logical_node', is_semantic=True,
                                      func=give_type_to_next_logical)
give_func_return_type_to_Stmts_node = Node('give_func_return_type_to_Stmts', is_semantic=True,
                                           func=give_func_return_type_to_stmts)
give_func_return_type_node = Node('give_func_return_type', is_semantic=True, func=give_func_return_type)
set_return_state_node = Node('set_return_state', is_semantic=True, func=set_return_state)
check_assignment_state_node = Node('check_assignment_state', is_semantic=True, func=check_assignment_state)
set_assignment_expected_type_node = Node('set_assignment_expected_type', is_semantic=True,
                                         func=set_assignment_expected_type)
get_id_type_node = Node('get_id_type', is_semantic=True, func=get_id_type)
give_base_type_to_bracket_node = Node('give_base_type_to_bracket', is_semantic=True, func=give_base_type_to_bracket)
set_bracket_type_inuse_node = Node('set_bracket_type_inuse', is_semantic=True, func=set_bracket_type_inuse)
set_bracket_type_inuse_end_node = Node('set_bracket_type_inuse_end', is_semantic=True,
                                       func=set_bracket_type_inuse_end)
check_mutable_type_node = Node('check_mutable_type', is_semantic=True, func=check_mutable_type)
set_bracket_type_in_exp_node = Node('set_bracket_type_in_exp', is_semantic=True,
                                    func=set_bracket_type_in_exp)
give_type_to_parent_mutable_or_function_node = Node('give_type_to_parent_mutable_or_function', is_semantic=True,
                                                    func=give_type_to_parent_mutable_or_function)
set_bracket_base_type_in_check_call_node = Node('set_bracket_base_type_in_check_call', is_semantic=True,
                                                func=set_bracket_base_type_in_check_call)
set_assignment_expected_type_for_bracket_node = Node('set_assignment_expected_type_for_bracket', is_semantic=True,
                                                     func=set_assignment_expected_type_for_bracket)
set_scope_for_function_params_node = Node('set_scope_for_function_params', is_semantic=True,
                                          func=set_scope_for_function_params)
give_scope_to_others_node = Node('give_scope_to_others', is_semantic=True, func=give_scope_to_others)
set_bracket_base_type_in_function_def_node = Node('set_bracket_base_type_in_function_def', is_semantic=True,
                                                  func=set_bracket_base_type_in_function_def)
add_parameter_node = Node('add_parameter', is_semantic=True, func=add_parameter)
set_args_list_node = Node('set_args_list', is_semantic=True, func=set_args_list)
add_argument_node = Node('add_argument', is_semantic=True, func=add_argument)
give_args_list_to_next_node = Node('give_args_list_to_next', is_semantic=True, func=give_args_list_to_next)
check_call_node = Node('check_call', is_semantic=True, func=check_call)
give_id_name_to_call_node = Node('give_id_name_to_call', is_semantic=True, func=give_id_name_to_call)
give_type_to_parent_in_call_node = Node('give_type_to_parent_in_call', is_semantic=True,
                                        func=give_type_to_parent_in_call)
set_stmts_scope_in_if_node = Node('set_stmts_scope_in_if', is_semantic=True, func=set_stmts_scope_in_if)
set_stmts_scope_in_else_node = Node('set_stmts_scope_in_else', is_semantic=True, func=set_stmts_scope_in_else)
set_pre_loop_scope_node = Node('set_pre_loop_scope', is_semantic=True, func=set_pre_loop_scope)
check_optional_expr_for_node = Node('check_optional_expr_for', is_semantic=True, func=check_optional_expr_for)
set_stmts_scope_in_for_node = Node('set_stmts_scope_in_for', is_semantic=True, func=set_stmts_scope_in_for)
set_new_scope_node = Node('set_new_scope', is_semantic=True, func=set_new_scope)
check_print_node = Node('check_print', is_semantic=True, func=check_print)


SDD: Final = {
    'Program': [
        ['function', 'Program'],
        ['epsilon', check_main_node],
    ],
    'function': [
        ['Type', 'T_Id', 'T_LP', set_scope_for_function_params_node, 'function_params', add_function_node, 'T_RP',
         'T_LC', give_func_return_type_to_Stmts_node, 'Stmts', 'T_RC'],
    ],
    'Type': [
        ['T_Int', set_type_node],
        ['T_Char', set_type_node],
        ['T_Bool', set_type_node],
    ],
    'function_params': [
        [give_scope_to_others_node, 'param', 'params_list'],
        ['epsilon'],
    ],
    'params_list': [
        [give_scope_to_others_node, 'T_Comma', 'param', 'params_list'],
        ['epsilon'],
    ],
    'param': [
        ['Type', 'T_Id', set_bracket_base_type_in_function_def_node, 'const_bracket', add_parameter_node],
    ],
    'const_bracket': [
        ['T_LB', 'const', 'T_RB', set_bracket_base_type_node, 'const_bracket', set_bracket_type_node],
        ['epsilon', set_bracket_type_end_node],
    ],
    'Stmts': [
        [give_func_return_type_node, 'stmt', 'Stmts'],
        ['epsilon'],
    ],
    'stmt': [
        [give_scope_to_others_node, 'Declaration', 'T_Semicolon'],
        [give_func_return_type_node, 'other_stmt'],
        ['Assignment', 'T_Semicolon'],
        [give_func_return_type_node, 'for_statement'],
        [give_func_return_type_node, 'if_statement'],
        ['print_statement', 'T_Semicolon'],
        ['unary_assignment', 'T_Semicolon'],
        [set_new_scope_node, 'T_LC', 'Stmts', 'T_RC'],
    ],
    'Declaration': [
        ['Type', set_declaration_expected_type_node, 'Declarations'],
    ],
    'Declarations': [
        [set_var_declaration_expected_type_node, 'var_declaration', 'Declaration_list'],
        ['epsilon'],
    ],
    'Declaration_list': [
        [set_var_declaration_expected_type_node, 'T_Comma', 'var_declaration', 'Declaration_list'],
        ['epsilon'],
    ],
    'var_declaration': [
        [set_var_declaration_expected_type_node, 'declare_mutable', 'Declaration_Assign', add_variable_node],
    ],
    'Declaration_Assign': [
        ['T_Assign', 'Exp', set_declaration_assign_node],
        ['epsilon', set_declaration_assign_node],
    ],
    'declare_mutable': [
        ['T_Id', set_bracket_base_type_node, 'const_bracket', set_declaration_var_node],
    ],
    'mutable': [
        ['T_Id', give_base_type_to_bracket_node, 'bracket', check_mutable_type_node],
    ],
    'bracket': [
        ['T_LB', 'Exp', 'T_RB', set_bracket_type_inuse_node, 'bracket', set_bracket_type_inuse_end_node],
        ['epsilon', set_bracket_type_inuse_end_node],
    ],
    'Assign': [
        ['T_Assign', 'Exp', check_assignment_state_node],
        ['T_AOp_PL', 'T_Assign', 'Exp', check_assignment_state_node],
        ['T_AOp_MN', 'T_Assign', 'Exp', check_assignment_state_node],
        ['T_AOp_ML', 'T_Assign', 'Exp', check_assignment_state_node],
        ['T_AOp_DV', 'T_Assign', 'Exp', check_assignment_state_node],
        ['T_AOp_RM', 'T_Assign', 'Exp', check_assignment_state_node],
        ['epsilon', check_assignment_state_node],
    ],
    'check_call': [
        [give_id_name_to_call_node, 'call'],
        [set_bracket_base_type_in_check_call_node, 'bracket', set_assignment_expected_type_for_bracket_node,
         'Assign'],
        [set_assignment_expected_type_node, 'Assign'],
    ],
    'other_stmt': [
        ['T_Break', 'T_Semicolon'],
        ['T_Continue', 'T_Semicolon'],
        ['T_Return', 'Exp', 'T_Semicolon', set_return_state_node],
    ],
    'Args': [
        [give_args_list_to_next_node, 'Exp', add_argument_node, 'Args_list'],
        ['epsilon'],
    ],
    'Args_list': [
        [give_args_list_to_next_node, 'T_Comma', 'Exp', add_argument_node, 'Args_list'],
        ['epsilon'],
    ],
    'Assignment': [
        ['T_Id', get_id_type_node, 'check_call'],
    ],
    'Exp': [
        ['and_expr', give_type_to_next_logical_node, 'A', give_type_to_parent_node],
    ],
    'A': [
        ['T_LOp_OR', 'and_expr', give_type_to_next_logical_node, 'A', give_type_to_parent_relational_node],
        ['epsilon', give_type_to_parent_end_node],
    ],
    'and_expr': [
        ['unary_expr', give_type_to_next_logical_node, 'B', give_type_to_parent_node],
    ],
    'B': [
        ['T_LOp_AND', 'unary_expr', give_type_to_next_logical_node, 'B', give_type_to_parent_relational_node],
        ['epsilon', give_type_to_parent_end_node],
    ],
    'unary_expr': [
        ['rel_expr', set_const_value_node],
    ],
    'rel_expr': [
        ['sum_expr', give_type_to_next_relational_node, 'C', give_type_to_parent_node],
    ],
    'C': [
        ['rel_op', 'sum_expr', give_type_to_next_relational_node, 'C', give_type_to_parent_relational_node],
        ['epsilon', give_type_to_parent_end_node],
    ],
    'rel_op': [
        ['T_ROp_L'],
        ['T_ROp_G'],
        ['T_ROp_LE'],
        ['T_ROp_GE'],
        ['T_ROp_NE'],
        ['T_ROp_E'],
    ],
    'sum_expr': [
        ['mul_expr', give_type_to_next_numeric_node, 'D', give_type_to_parent_node],
    ],
    'D': [
        ['sum_op', 'mul_expr', give_type_to_next_numeric_node, 'D', give_type_to_parent_node],
        ['epsilon', give_type_to_parent_end_node],
    ],
    'sum_op': [
        ['T_AOp_PL'],
        ['T_AOp_MN'],
    ],
    'mul_expr': [
        ['factor', give_type_to_next_numeric_node, 'E', give_type_to_parent_node],
    ],
    'E': [
        ['mul_op', 'factor', give_type_to_next_numeric_node, 'E', give_type_to_parent_node],
        ['epsilon', give_type_to_parent_end_node],
    ],
    'mul_op': [
        ['T_AOp_ML'],
        ['T_AOp_DV'],
        ['T_AOp_RM'],
    ],
    'factor': [
        ['immutable', set_const_value_node],
        ['T_Id', set_bracket_type_in_exp_node, 'mutable_or_function_call', give_type_to_parent_mutable_or_function_node],
    ],
    'mutable_or_function_call': [
        [set_var_declaration_expected_type_node, 'bracket', set_bracket_type_inuse_end_node],
        [give_id_name_to_call_node, 'call', give_type_to_parent_in_call_node],
        ['epsilon', set_bracket_type_inuse_end_node],
    ],
    'call': [
        ['T_LP', set_args_list_node, 'Args', 'T_RP', check_call_node],
    ],
    'immutable': [
        ['T_LP', 'Exp', 'T_RP', set_immutable_type_numeric],
        ['const', set_const_value_node],
        ['T_AOp_PL', 'factor', set_immutable_type_numeric_node],
        ['T_AOp_MN', 'factor', set_immutable_type_numeric_node],
        ['T_LOp_NOT', 'rel_expr', set_immutable_type_relational_node],
    ],
    'const': [
        ['T_Character', set_const_value_node],
        ['T_String', set_const_value_node],
        ['T_True', set_const_value_node],
        ['T_False', set_const_value_node],
        ['T_Decimal', set_const_value_node],
        ['T_Hexadecimal', set_const_value_node],
    ],
    'for_statement': [
        ['T_For', 'T_LP', set_pre_loop_scope_node, 'pre_loop', 'T_Semicolon', 'optional_expr', 'T_Semicolon',
         'optional_assignment', 'T_RP', 'T_LC', set_stmts_scope_in_for_node, 'Stmts', 'T_RC'],
    ],
    'pre_loop': [
        [give_scope_to_others_node, 'Declaration'],
        ['Assignment'],
        ['epsilon'],
    ],
    'optional_expr': [
        ['Exp', check_optional_expr_for_node],
        ['epsilon'],
    ],
    'optional_assignment': [
        ['Assignment'],
        ['unary_assignment'],
        ['epsilon'],
    ],
    'if_statement': [
        ['T_If', 'T_LP', 'Exp', 'T_RP', 'T_LC', set_stmts_scope_in_if_node, 'Stmts', 'T_RC', 'else_if'],
    ],
    'else_if': [
        [give_func_return_type_node, 'T_Else', 'check_if'],
        ['epsilon'],
    ],
    'check_if': [
        [give_func_return_type_node, 'if_statement'],
        [give_func_return_type_node, 'statement'],
    ],
    'statement': [
        ['T_LC', set_stmts_scope_in_else_node, 'Stmts', 'T_RC'],
    ],
    'print_statement': [
        ['T_Print', 'T_LP', set_args_list_node, 'Args', 'T_RP', check_print_node],
    ],
    'unary_assignment': [
        ['T_AOp_PL', 'T_AOp_PL', 'mutable'],
        ['T_AOp_MN', 'T_AOp_MN', 'mutable'],
    ]
}


def add_semantic_nodes(syntax_tree: Node):
    children = list(syntax_tree.children)
    for rule in SDD[syntax_tree.name]:
        rule_index = 1 if isinstance(rule[0], Node) else 0
        if children[0].name == rule[rule_index]:
            for idx, _ in enumerate(rule):
                if isinstance(_, Node):
                    children.insert(idx, deepcopy(_))

    syntax_tree.children = children
    for node in syntax_tree.children:
        if not node.is_semantic and not node.is_leaf:
            add_semantic_nodes(node)

"""
    Here we will have the SDD for the PL language.
    This implementation is used for PL Language Compiler (PL) semantic analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import Final
from syntax_analyzer.special_node import Node
from semantic_analyzer.node_functions import add_function, set_function_attributes
from copy import deepcopy

add_function_node = Node('add_function', is_semantic=True)
add_function_node.run = add_function

set_function_node = Node('set_function', is_semantic=True)
set_function_node.run = set_function_attributes

SDD: Final = {
    'Program': [
        ['function', add_function_node, 'Program'],
        ['epsilon'],
    ],
    'function': [
        ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC', set_function_node],
    ],
    'Type': [
        ['T_Int'],
        ['T_Char'],
        ['T_Bool'],
    ],
    'function_params': [
        ['param', 'params_list'],
        ['epsilon'],
    ],
    'params_list': [
        ['T_Comma', 'param', 'params_list'],
        ['epsilon'],
    ],
    'param': [
        ['Type', 'T_Id', 'const_bracket'],
    ],
    'const_bracket': [
        ['T_LB', 'const', 'T_RB', 'const_bracket'],
        ['epsilon'],
    ],
    'Stmts': [
        ['stmt', 'Stmts'],
        ['epsilon'],
    ],
    'stmt': [
        ['Declaration', 'T_Semicolon'],
        ['other_stmt'],
        ['Assignment', 'T_Semicolon'],
        ['for_statement'],
        ['if_statement'],
        ['print_statement', 'T_Semicolon'],
        ['unary_assignment', 'T_Semicolon'],
    ],
    'Declaration': [
        ['Type', 'Declarations'],
    ],
    'Declarations': [
        ['var_declaration', 'Declaration_list'],
        ['epsilon'],
    ],
    'Declaration_list': [
        ['T_Comma', 'var_declaration', 'Declaration_list'],
        ['epsilon'],
    ],
    'var_declaration': [
        ['declare_mutable', 'Declaration_Assign'],
    ],
    'Declaration_Assign': [
        ['T_Assign', 'Exp'],
        ['epsilon'],
    ],
    'declare_mutable': [
        ['T_Id', 'const_bracket'],
    ],
    'mutable': [
        ['T_Id', 'bracket'],
    ],
    'bracket': [
        ['T_LB', 'Exp', 'T_RB', 'bracket'],
        ['epsilon'],
    ],
    'Assign': [
        ['T_Assign', 'Exp'],
        ['T_AOp_PL', 'T_Assign', 'Exp'],
        ['T_AOp_MN', 'T_Assign', 'Exp'],
        ['T_AOp_ML', 'T_Assign', 'Exp'],
        ['T_AOp_DV', 'T_Assign', 'Exp'],
        ['T_AOp_RM', 'T_Assign', 'Exp'],
        ['epsilon'],
    ],
    'check_call': [
        ['call'],
        ['bracket', 'Assign'],
        ['Assign'],
    ],
    'other_stmt': [
        ['T_Break', 'T_Semicolon'],
        ['T_Continue', 'T_Semicolon'],
        ['T_Return', 'Exp', 'T_Semicolon'],
    ],
    'Args': [
        ['Exp', 'Args_list'],
        ['epsilon'],
    ],
    'Args_list': [
        ['T_Comma', 'Exp', 'Args_list'],
        ['epsilon'],
    ],
    'Assignment': [
        ['T_Id', 'check_call'],
    ],
    'Exp': [
        ['and_expr', 'A'],
    ],
    'A': [
        ['T_LOp_OR', 'and_expr', 'A'],
        ['epsilon'],
    ],
    'and_expr': [
        ['unary_expr', 'B'],
    ],
    'B': [
        ['T_LOp_AND', 'unary_expr', 'B'],
        ['epsilon'],
    ],
    'unary_expr': [
        ['rel_expr'],
    ],
    'rel_expr': [
        ['sum_expr', 'C'],
    ],
    'C': [
        ['rel_op', 'sum_expr', 'C'],
        ['epsilon'],
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
        ['mul_expr', 'D'],
    ],
    'D': [
        ['sum_op', 'mul_expr', 'D'],
        ['epsilon'],
    ],
    'sum_op': [
        ['T_AOp_PL'],
        ['T_AOp_MN'],
    ],
    'mul_expr': [
        ['factor', 'E'],
    ],
    'E': [
        ['mul_op', 'factor', 'E'],
        ['epsilon'],
    ],
    'mul_op': [
        ['T_AOp_ML'],
        ['T_AOp_DV'],
        ['T_AOp_RM'],
    ],
    'factor': [
        ['immutable'],
        ['T_Id', 'mutable_or_function_call'],
    ],
    'mutable_or_function_call': [
        ['bracket'],
        ['call'],
        ['epsilon'],
    ],
    'call': [
        ['T_LP', 'Args', 'T_RP'],
    ],
    'immutable': [
        ['T_LP', 'Exp', 'T_RP'],
        ['const'],
        ['T_AOp_PL', 'factor'],
        ['T_AOp_MN', 'factor'],
        ['T_LOp_NOT', 'rel_expr'],
    ],
    'const': [
        ['T_Character'],
        ['T_String'],
        ['T_True'],
        ['T_False'],
        ['T_Decimal'],
        ['T_Hexadecimal'],
    ],
    'for_statement': [
        ['T_For', 'T_LP', 'pre_loop', 'T_Semicolon', 'optional_expr', 'T_Semicolon', 'optional_assignment',
                  'T_RP', 'T_LC', 'Stmts', 'T_RC'],
    ],
    'pre_loop': [
        ['Declaration'],
        ['Assignment'],
        ['epsilon'],
    ],
    'optional_expr': [
        ['Exp'],
        ['epsilon'],
    ],
    'optional_assignment': [
        ['Assignment'],
        ['unary_assignment'],
        ['epsilon'],
    ],
    'if_statement': [
        ['T_If', 'T_LP', 'Exp', 'T_RP', 'T_LC', 'Stmts', 'T_RC', 'else_if'],
    ],
    'else_if': [
        ['T_Else', 'check_if'],
        ['epsilon'],
    ],
    'check_if': [
        ['if_statement'],
        ['statement'],
    ],
    'statement': [
        ['T_LC', 'Stmts', 'T_RC'],
    ],
    'print_statement': [
        ['T_Print', 'T_LP', 'Args', 'T_RP'],
    ],
    'unary_assignment': [
        ['T_AOp_PL', 'T_AOp_PL', 'mutable'],
        ['T_AOp_MN', 'T_AOp_MN', 'mutable'],
    ]
}


def add_semantic_nodes(syntax_tree: Node):
    children = list(syntax_tree.children)
    for rule in SDD[syntax_tree.name]:
        if children[0].name == rule[0]:
            for idx, _ in enumerate(rule):
                if isinstance(_, Node):
                    children.insert(idx, deepcopy(_))

    syntax_tree.children = children
    for node in syntax_tree.children:
        if not node.is_semantic and not node.is_leaf:
            add_semantic_nodes(node)


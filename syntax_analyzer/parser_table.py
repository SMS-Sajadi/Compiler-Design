"""
    Here we will have the Parser Table that the syntax analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""

VARS = ['Program', 'functions', 'Type', 'function_params', 'Stmts', 'param', 'params_list', 'const_bracket',
        'Stmts', 'stmt', 'Declaration', 'Declarations', ]

M = {
    'Program': {
        # First
        'T_Int': ['function', 'Program'],
        'T_Char': ['function', 'Program'],
        'T_Bool': ['function', 'Program'],
        # Follow
        '$': ['epsilon'],
    },
    'function': {
        # First
        'T_Int': ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC'],
        'T_Char': ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC'],
        'T_Bool': ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC'],
    },
    'Type': {
        # First
        'T_Int': ['T_Int'],
        'T_Char': ['T_Char'],
        'T_Bool': ['T_Bool'],
    },
    'function_params': {
        # First
        'T_Int': ['param', 'params_list'],
        'T_Char': ['param', 'params_list'],
        'T_Bool': ['param', 'params_list'],
        # Follow
        'T_RP': ['epsilon'],
    },
    'params_list': {
        # First
        'T_Comma': ['T_Comma', 'param', 'params_list'],
        # Follow
        'T_RP': ['epsilon'],
    },
    'param': {
        # First
        'T_Int': ['Type', 'T_Id', 'const_bracket'],
        'T_Char': ['Type', 'T_Id', 'const_bracket'],
        'T_Bool': ['Type', 'T_Id', 'const_bracket'],
    },
    'const_bracket': {
        # First
        'T_LB': ['T_LB', 'const', 'T_RB', 'const_bracket'],
        # Follow
        'T_Comma': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'Stmts': {
        # First
        'T_Int': ['stmt', 'Stmts'],
        'T_Char': ['stmt', 'Stmts'],
        'T_Bool': ['stmt', 'Stmts'],
        'T_Break': ['stmt', 'Stmts'],
        'T_Continue': ['stmt', 'Stmts'],
        'T_Return': ['stmt', 'Stmts'],
        'T_Id': ['stmt', 'Stmts'],
        'T_For': ['stmt', 'Stmts'],
        'T_If': ['stmt', 'Stmts'],
        'T_Print': ['stmt', 'Stmts'],
        # Follow
        'T_RC': ['epsilon'],
    },
    'stmt': {
        # First
        'T_Int': ['Declaration', 'T_Semicolon'],
        'T_Char': ['Declaration', 'T_Semicolon'],
        'T_Bool': ['Declaration', 'T_Semicolon'],
        'T_Break': ['other_stmt'],
        'T_Continue': ['other_stmt'],
        'T_Return': ['other_stmt'],
        'T_Id': ['Assignment', 'T_Semicolon'],
        'T_For': ['for_statement'],
        'T_If': ['if_statement'],
        'T_Print': ['print_statement', 'T_Semicolon'],
    },
    'Declaration': {
        # First
        'T_Int': ['Type', 'Declarations'],
        'T_Char': ['Type', 'Declarations'],
        'T_Bool': ['Type', 'Declarations'],
    },
    'Declarations': {
        # First
        'T_Id': ['var_declaration', 'Declaration_list'],
        # Follow
        'T_Semicolon': ['epsilon'],
    },
    'Declaration_list': {
        # First
        'T_Comma': ['T_Comma', 'var_declaration', 'Declaration_list'],
        # Follow
        'T_Semicolon': ['epsilon'],
    },
    'var_declaration': {
        # First
        'T_Id': ['mutable', 'Assign'],
    },
    'mutable': {
        # First
        'T_Id': ['T_Id', 'bracket'],
    },
    'bracket': {
        # First
        'T_LB': ['T_LB', 'Exp', 'T_RB', 'bracket'],
        # Follow
        'T_Assign': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_Semicolon': ['epsilon'],
    },
    'Assign': {
        # First
        'T_Assign': ['T_Assign', 'Exp'],
        # Follow
        'T_Comma': ['epsilon'],
        'T_Semicolon': ['epsilon'],
    },
    'check_call': {
        # First
        'T_LP': ['call'],
        'T_Assign': ['Assign'],
    },
    'other_stmt': {
        # First
        'T_Break': ['T_Break', 'T_Semicolon'],
        'T_Continue': ['T_Continue', 'T_Semicolon'],
        'T_Return': ['T_Return', 'Exp', 'T_Semicolon'],
    },
    'function_call': {
        # First
        'T_Id': ['T_Id', 'T_LP', 'Args', 'T_RP'],
    },
    'Args': {
        # First
        'T_Id': ['Exp', 'Args_list'],
        'T_LOp_NOT': ['Exp', 'Args_list'],
        'T_LP': ['Exp', 'Args_list'],
        'T_Character': ['Exp', 'Args_list'],
        'T_String': ['Exp', 'Args_list'],
        'T_True': ['Exp', 'Args_list'],
        'T_False': ['Exp', 'Args_list'],
        'T_Decimal': ['Exp', 'Args_list'],
        'T_Hexadecimal': ['Exp', 'Args_list'],
        'T_AOp_PL': ['Exp', 'Args_list'],
        'T_AOp_MN': ['Exp', 'Args_list'],
        # Follow
        'T_RP': ['epsilon'],
    },
    'Args_list': {
        # First
        'T_Comma': ['T_Comma', 'Exp', 'Args_list'],
        # Follow
        'T_RP': ['epsilon'],
    },
    'Assignment': {
        # First
        'T_Id': ['T_Id', 'check_call'],
    },
    'Exp': {
        # First
        'T_LOp_NOT': ['and_expr', 'A'],
        'T_Id': ['and_expr', 'A'],
        'T_LP': ['and_expr', 'A'],
        'T_Character': ['and_expr', 'A'],
        'T_String': ['and_expr', 'A'],
        'T_True': ['and_expr', 'A'],
        'T_False': ['and_expr', 'A'],
        'T_Decimal': ['and_expr', 'A'],
        'T_Hexadecimal': ['and_expr', 'A'],
        'T_AOp_PL': ['and_expr', 'A'],
        'T_AOp_MN': ['and_expr', 'A'],
    },
    'A': {
        # First
        'T_LOp_OR': ['T_LOp_OR', 'and_expr', 'A'],
        # Follow
        'T_Semicolon': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_RB': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'and_expr': {
        # First
        'T_LOp_NOT': ['unary_expr', 'B'],
        'T_Id': ['unary_expr', 'B'],
        'T_LP': ['unary_expr', 'B'],
        'T_Character': ['unary_expr', 'B'],
        'T_String': ['unary_expr', 'B'],
        'T_True': ['unary_expr', 'B'],
        'T_False': ['unary_expr', 'B'],
        'T_Decimal': ['unary_expr', 'B'],
        'T_Hexadecimal': ['unary_expr', 'B'],
        'T_AOp_PL': ['unary_expr', 'B'],
        'T_AOp_MN': ['unary_expr', 'B'],
    },
    'B': {
        # First
        'T_LOp_AND': ['T_LOp_AND', 'unary_expr', 'B'],
        # Follow
        'T_LOp_OR': ['epsilon'],
        'T_Semicolon': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_RB': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'unary_expr': {
        # First
        'T_LOp_NOT': ['T_LOp_NOT', 'unary_expr'],
        # # for unary_expr -> rel_expr
        'T_Id': ['rel_expr'],
        'T_LP': ['rel_expr'],
        'T_Character': ['rel_expr'],
        'T_String': ['rel_expr'],
        'T_True': ['rel_expr'],
        'T_False': ['rel_expr'],
        'T_Decimal': ['rel_expr'],
        'T_Hexadecimal': ['rel_expr'],
        'T_AOp_PL': ['rel_expr'],
        'T_AOp_MN': ['rel_expr'],
    },
    'rel_expr': {
        # First
        'T_Id': ['sum_expr', 'C'],
        'T_LP': ['sum_expr', 'C'],
        'T_Character': ['sum_expr', 'C'],
        'T_String': ['sum_expr', 'C'],
        'T_True': ['sum_expr', 'C'],
        'T_False': ['sum_expr', 'C'],
        'T_Decimal': ['sum_expr', 'C'],
        'T_Hexadecimal': ['sum_expr', 'C'],
        'T_AOp_PL': ['sum_expr', 'C'],
        'T_AOp_MN': ['sum_expr', 'C'],
    },
    'C': {
        # First
        'T_ROp_L': ['rel_op', 'sum_expr', 'C'],
        'T_ROp_G': ['rel_op', 'sum_expr', 'C'],
        'T_ROp_LE': ['rel_op', 'sum_expr', 'C'],
        'T_ROp_GE': ['rel_op', 'sum_expr', 'C'],
        'T_ROp_NE': ['rel_op', 'sum_expr', 'C'],
        'T_ROp_E': ['rel_op', 'sum_expr', 'C'],
        # Follow
        'T_LOp_AND': ['epsilon'],
        'T_LOp_OR': ['epsilon'],
        'T_Semicolon': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_RB': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'rel_op': {
        'T_ROp_L': ['T_ROp_L'],
        'T_ROp_G': ['T_ROp_G'],
        'T_ROp_LE': ['T_ROp_LE'],
        'T_ROp_GE': ['T_ROp_GE'],
        'T_ROp_NE': ['T_ROp_NE'],
        'T_ROp_E': ['T_ROp_E'],
    },
    'sum_expr': {
        # First
        'T_Id': ['mul_expr', 'D'],
        'T_LP': ['mul_expr', 'D'],
        'T_Character': ['mul_expr', 'D'],
        'T_String': ['mul_expr', 'D'],
        'T_True': ['mul_expr', 'D'],
        'T_False': ['mul_expr', 'D'],
        'T_Decimal': ['mul_expr', 'D'],
        'T_Hexadecimal': ['mul_expr', 'D'],
        'T_AOp_PL': ['mul_expr', 'D'],
        'T_AOp_MN': ['mul_expr', 'D'],
    },
    'D': {
        # First
        'T_AOp_PL': ['sum_op', 'mul_expr', 'D'],
        'T_AOp_MN': ['sum_op', 'mul_expr', 'D'],
        # Follow
        'T_ROp_L': ['epsilon'],
        'T_ROp_G': ['epsilon'],
        'T_ROp_LE': ['epsilon'],
        'T_ROp_GE': ['epsilon'],
        'T_ROp_NE': ['epsilon'],
        'T_ROp_E': ['epsilon'],
        'T_LOp_AND': ['epsilon'],
        'T_LOp_OR': ['epsilon'],
        'T_Semicolon': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_RB': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'sum_op': {
        # First
        'T_AOp_PL': ['T_AOp_PL'],
        'T_AOp_MN': ['T_AOp_MN'],
    },
    'mul_expr': {
        # First
        'T_Id': ['factor', 'E'],
        'T_LP': ['factor', 'E'],
        'T_Character': ['factor', 'E'],
        'T_String': ['factor', 'E'],
        'T_True': ['factor', 'E'],
        'T_False': ['factor', 'E'],
        'T_Decimal': ['factor', 'E'],
        'T_Hexadecimal': ['factor', 'E'],
        'T_AOp_PL': ['factor', 'E'],
        'T_AOp_MN': ['factor', 'E'],
    },
    'E': {
        # First
        'T_AOp_ML': ['mul_op', 'factor', 'E'],
        'T_AOp_DV': ['mul_op', 'factor', 'E'],
        'T_AOp_RM': ['mul_op', 'factor', 'E'],
        # Follow
        'T_AOp_PL': ['epsilon'],
        'T_AOp_MN': ['epsilon'],
        'T_ROp_L': ['epsilon'],
        'T_ROp_G': ['epsilon'],
        'T_ROp_LE': ['epsilon'],
        'T_ROp_GE': ['epsilon'],
        'T_ROp_NE': ['epsilon'],
        'T_ROp_E': ['epsilon'],
        'T_LOp_AND': ['epsilon'],
        'T_LOp_OR': ['epsilon'],
        'T_Semicolon': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_RB': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'mul_op': {
        'T_AOp_ML': ['T_AOp_ML'],
        'T_AOp_DV': ['T_AOp_DV'],
        'T_AOp_RM': ['T_AOp_RM'],
    },
    'factor': {
        # First
        'T_LP': ['immutable'],
        'T_String': ['immutable'],
        'T_True': ['immutable'],
        'T_False': ['immutable'],
        'T_Decimal': ['immutable'],
        'T_Hexadecimal': ['immutable'],
        'T_Character': ['immutable'],
        # # For +/-(exp)
        'T_AOp_PL': ['immutable'],
        'T_AOp_MN': ['immutable'],
        'T_Id': ['T_Id', 'mutable_or_function_call'],
    },
    'mutable_or_function_call': {
        # First
        'T_LB': ['bracket'],
        'T_LP': ['call'],
        # Follow
        'T_AOp_ML': ['epsilon'],
        'T_AOp_DV': ['epsilon'],
        'T_AOp_RM': ['epsilon'],
        'T_AOp_PL': ['epsilon'],
        'T_AOp_MN': ['epsilon'],
        'T_ROp_L': ['epsilon'],
        'T_ROp_G': ['epsilon'],
        'T_ROp_LE': ['epsilon'],
        'T_ROp_GE': ['epsilon'],
        'T_ROp_NE': ['epsilon'],
        'T_ROp_E': ['epsilon'],
        'T_LOp_AND': ['epsilon'],
        'T_LOp_OR': ['epsilon'],
        'T_Semicolon': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_RB': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'call': {
        # First
        'T_LP': ['T_LP', 'Args', 'T_RP'],
    },
    'immutable': {
        # First
        'T_LP': ['T_LP', 'Exp', 'T_RP'],
        'T_Character': ['const'],
        'T_String': ['const'],
        'T_True': ['const'],
        'T_False': ['const'],
        'T_Decimal': ['const'],
        'T_Hexadecimal': ['const'],
        # # For +/-op
        'T_AOp_PL': ['T_AOp_PL', 'Exp'],
        'T_AOp_MN': ['T_AOp_MN', 'Exp'],
    },
    'const': {
        # First
        'T_Character': ['T_Character'],
        'T_String': ['T_String'],
        'T_True': ['T_True'],
        'T_False': ['T_False'],
        'T_Decimal': ['T_Decimal'],
        'T_Hexadecimal': ['T_Hexadecimal'],
    },
    'for_statement': {
        # First
        'T_For': ['T_For', 'T_LP', 'pre_loop', 'T_Semicolon', 'optional_expr', 'T_Semicolon', 'optional_assignment',
                  'T_RP', 'T_LC', 'Stmts', 'T_RC'],
    },
    'pre_loop': {
        # First
        'T_Int': ['Declaration'],
        'T_Char': ['Declaration'],
        'T_Bool': ['Declaration'],
        'T_Id': ['Assignment'],
        # Follow
        'T_Semicolon': ['epsilon'],
    },
    'optional_expr': {
        # First
        'T_LOp_NOT': ['Exp'],
        'T_Id': ['Exp'],
        'T_LP': ['Exp'],
        'T_Character': ['Exp'],
        'T_String': ['Exp'],
        'T_True': ['Exp'],
        'T_False': ['Exp'],
        'T_Decimal': ['Exp'],
        'T_Hexadecimal': ['Exp'],
        'T_AOp_PL': ['Exp'],
        'T_AOp_MN': ['Exp'],
        # Follow
        'T_Semicolon': ['epsilon'],
    },
    'optional_assignment': {
        # First
        'T_Id': ['Assignment'],
        # Follow
        'T_RP': ['epsilon'],
    },
    'if_statement': {
        # First
        'T_If': ['T_If', 'T_LP', 'Exp', 'T_RP', 'T_LC', 'Stmts', 'T_RC', 'else_if'],
    },
    'else_if': {
        # First
        'T_Else': ['T_Else', 'check_if'],
        # Follow
        # TODO: Complete, First(Stmts) + Follow(Stmts)
        'T_Int': ['epsilon'],
        'T_Char': ['epsilon'],
        'T_Bool': ['epsilon'],
        'T_Break': ['epsilon'],
        'T_Continue': ['epsilon'],
        'T_Return': ['epsilon'],
        'T_Id': ['epsilon'],
        'T_For': ['epsilon'],
        'T_If': ['epsilon'],
        'T_Print': ['epsilon'],
        'T_RC': ['epsilon'],
    },
    'check_if': {
        # First
        'T_If': ['if_statement'],
        'T_LC': ['statement'],
    },
    'statement': {
        # First
        'T_LC': ['T_LC', 'Stmts', 'T_RC'],
    },
    'print_statement': {
        # First
        'T_Print': ['T_Print', 'T_LP', 'Args', 'T_RP'],
    }
    # TODO: Continue to Infinity!
    # TODO: Complete the Stmts ans stmt
    # TODO: Check Semicolons
    # TODO: ADD ++ and -- statements (optional)
}


def get_table():
    """
    This function is used to generate the syntax analyzer table.
    :return: The syntax analyzer table.
    """

    return M

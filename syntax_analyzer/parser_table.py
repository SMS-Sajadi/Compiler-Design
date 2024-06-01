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
        'T_LB': ['T_LB', 'const_num', 'T_RB', 'const_bracket'],
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
        # Follow
        'T_RC': ['epsilon'],
    },
    'Declaration': {
        # First
        'T_Int': ['Type', 'Declarations', 'T_Semicolon'],
        'T_Char': ['Type', 'Declarations', 'T_Semicolon'],
        'T_Bool': ['Type', 'Declarations', 'T_Semicolon'],
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
    'stmt': {
        # First
        'T_Int': ['Declaration'],
        'T_Char': ['Declaration'],
        'T_Bool': ['Declaration'],
        'T_Break': ['other_stmt'],
        'T_Continue': ['other_stmt'],
        'T_Return': ['other_stmt'],
        'T_Id': ['function_call', 'T_Semicolon']
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
        # TODO: Continue first of Expr
        # Follow
        'T_RP': ['epsilon'],
    },
    'Args_list': {
        # First
        'T_Comma': ['T_Comma', 'Exp', 'Args_list'],
        # Follow
        'T_RP': ['epsilon'],
    }
    # TODO: Continue to Infinity!
    # TODO: Write const_num
    # TODO: Complete the Stmts ans stmt
    # TODO: Write Exp
    # TODO: Check Semicolons
}


def get_table():
    """
    This function is used to generate the syntax analyzer table.
    :return: The syntax analyzer table.
    """

    return M

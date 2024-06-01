"""
    Here we will have the Parser Table that the syntax analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""

VARS = ['Program', 'functions', 'Type', 'function_params', 'Stmts', 'param', 'params_list', 'const_bracket']

M = {
    'Program': {
        'T_Int': ['function', 'Program'],
        'T_Char': ['function', 'Program'],
        'T_Bool': ['function', 'Program'],
        '$': ['epsilon'],
    },
    'function': {
        'T_Int': ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC'],
        'T_Char': ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC'],
        'T_Bool': ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC'],
    },
    'Type': {
        'T_Int': ['T_Int'],
        'T_Char': ['T_Char'],
        'T_Bool': ['T_Bool'],
    },
    'function_params': {
        'T_Int': ['param', 'params_list'],
        'T_Char': ['param', 'params_list'],
        'T_Bool': ['param', 'params_list'],
        'T_RP': ['epsilon'],
    },
    'params_list': {
        'T_Comma': ['T_Comma', 'param', 'params_list'],
        'T_RP': ['epsilon'],
    },
    'param': {
        'T_Int': ['Type', 'T_Id', 'const_bracket'],
        'T_Char': ['Type', 'T_Id', 'const_bracket'],
        'T_Bool': ['Type', 'T_Id', 'const_bracket'],
    },
    'const_bracket': {
        'T_LB': ['T_LB', 'const_num', 'T_RB', 'const_bracket'],
        'T_Comma': ['epsilon'],
        'T_RP': ['epsilon'],
    },
    'Stmts': {
        # First
        'T_Int': ['stmt', 'Stmts'],
        'T_Char': ['stmt', 'Stmts'],
        'T_Bool': ['stmt', 'Stmts'],
        # Follow
        'T_RC': ['epsilon'],
    },
    'Declaration': {
        'T_Int': ['Type', 'Declarations', 'T_Semicolon'],
        'T_Char': ['Type', 'Declarations', 'T_Semicolon'],
        'T_Bool': ['Type', 'Declarations', 'T_Semicolon'],
    },
    'Declarations': {
        'T_Id': ['var_declaration', 'Declaration_list'],
        'T_Semicolon': ['epsilon'],
    },
    'Declaration_list': {
        'T_Comma': ['T_Comma', 'var_declaration', 'Declaration_list'],
        'T_Semicolon': ['epsilon'],
    },
    'var_declaration': {
        'T_Id': ['mutable', 'Assign'],
    },
    'mutable': {
        'T_Id': ['T_Id', 'bracket'],
    },
    'bracket': {
        'T_LB': ['T_LB', 'Exp', 'T_RB', 'bracket'],
        'T_Assign': ['epsilon'],
        'T_Comma': ['epsilon'],
        'T_Semicolon': ['epsilon'],
    },
    'Assign': {
        'T_Assign': ['T_Assign', 'Exp'],
        'T_Comma': ['epsilon'],
        'T_Semicolon': ['epsilon'],
    },
    'stmt': {
        'T_Int': ['Declaration'],
        'T_Char': ['Declaration'],
        'T_Bool': ['Declaration'],
    }
    # TODO: Continue to Infinity!
    # TODO: Write const_num
}


def get_table():
    """
    This function is used to generate the syntax analyzer table.
    :return: The syntax analyzer table.
    """

    return M

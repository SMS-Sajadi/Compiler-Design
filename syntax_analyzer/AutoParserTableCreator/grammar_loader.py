"""
    Here we will have the base structure for Grammar Loader that the syntax analyzer uses.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import Final, Set, Dict


TOKENS: Final = ['T_Bool', 'T_Break', 'T_Char', 'T_Continue', 'T_Else', 'T_False', 'T_For', 'T_If', 'T_Int', 'T_Print',
                 'T_Return', 'T_True', 'T_AOp_PL', 'T_AOp_MN', 'T_AOp_ML', 'T_AOp_DV', 'T_AOp_RM', 'T_ROp_L', 'T_ROp_G',
                 'T_ROp_LE', 'T_ROp_GE', 'T_ROp_NE', 'T_ROp_E', 'T_LOp_AND', 'T_LOp_OR', 'T_LOp_NOT', 'T_Assign',
                 'T_LP', 'T_RP', 'T_LC', 'T_RC', 'T_LB', 'T_RB', 'T_Semicolon', 'T_Comma', 'T_Id', 'T_Decimal',
                 'T_Hexadecimal', 'T_String', 'T_Character', 'epsilon']


RAW_GRAMMAR: Final = {
    'Program': [
        ['function', 'Program'],
        ['epsilon'],
    ],
    'function': [
        ['Type', 'T_Id', 'T_LP', 'function_params', 'T_RP', 'T_LC', 'Stmts', 'T_RC'],
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
        ['T_LC', 'Stmts', 'T_RC'],
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

firsts: Dict[str, Set] = {}
follows = {}


def regulizer(a):
    a['E']['T_AOp_ML'] = ['mul_op', 'factor', 'E']
    a['E']['T_AOp_DV'] = ['mul_op', 'factor', 'E']
    a['E']['T_AOp_RM'] = ['mul_op', 'factor', 'E']


def first_calculator(head):
    rules = RAW_GRAMMAR[head]
    for rule in rules:
        for idx, symbol in enumerate(rule):
            if symbol in TOKENS:
                if head in firsts:
                    firsts[head].add(symbol)
                else:
                    firsts[head] = {symbol}
                break

            first_calculator(symbol)
            if 'epsilon' not in firsts[symbol] or idx == len(rule) - 1:
                if head in firsts:
                    firsts[head] = firsts[head].union(firsts[symbol])
                else:
                    firsts[head] = firsts[symbol].copy()
                break
            else:
                if head in firsts:
                    firsts[head] = firsts[head].union(firsts[symbol] - {'epsilon'})
                else:
                    firsts[head] = firsts[symbol].copy() - {'epsilon'}


def follow_calculator(head):

    for rule_set in RAW_GRAMMAR:
        for rule in RAW_GRAMMAR[rule_set]:
            if head in rule:
                idx = rule.index(head)
                for index in range(idx, len(rule)):
                    if index == len(rule) - 1:
                        if rule_set not in follows:
                            follow_calculator(rule_set)

                        if head in follows:
                            follows[head] = follows[head].union(follows[rule_set])
                        else:
                            follows[head] = follows[rule_set].copy()
                        break

                    if head in follows:
                        follows[head] = follows[head].union(firsts[rule[index + 1]] - {'epsilon'})

                        if 'epsilon' not in firsts[rule[index + 1]]:
                            break
                    else:
                        follows[head] = firsts[rule[index + 1]].copy() - {'epsilon'}

                        if 'epsilon' not in firsts[rule[index + 1]]:
                            break


def first_and_follow_calculator():
    for rule_set in RAW_GRAMMAR:
        first_calculator(rule_set)

    follows['Program'] = {'$'}
    for token in TOKENS:
        firsts[token] = {token}

    for rule_set in RAW_GRAMMAR:
        follow_calculator(rule_set)


def get_auto_table():
    first_and_follow_calculator()

    table = {}

    for rule_set in RAW_GRAMMAR:
        table[rule_set] = {}
        for rule in RAW_GRAMMAR[rule_set]:
            rule_first = set()
            for idx in range(len(rule)):
                rule_first = rule_first.union(firsts[rule[idx]])

                if 'epsilon' not in firsts[rule[idx]]:
                    break

            if 'epsilon' in rule_first:
                if '$' in follows[rule_set]:
                    table[rule_set]['$'] = rule
                for _ in follows[rule_set]:
                    table[rule_set][_] = rule

            for _ in rule_first - {'epsilon'}:
                table[rule_set][_] = rule

        for _ in follows[rule_set]:
            if _ not in table[rule_set]:
                table[rule_set][_] = ['synch']

    regulizer(table)
    return table

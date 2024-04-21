"""
    In this file, there is a function which implements the lexical analyzer for the PL Language.
    This implementation is used for PL Language Compiler (PL) lexical analyzer, and
    should not be used directly.
    (c) 2024|1403
"""
from typing import List
from lexical_analyzer.token_base import Token
from lexical_analyzer import lexeme_detectors as ld


def tokenize(program: str) -> List[Token]:
    """
    Tokenize a program into a list of tokens.
    :param program: The program source code.
    :return: List of tokens.
    """
    tokens: List[Token] = []

    # TODO: Set to 0
    lexeme_begin: int = 0
    line: int = 1
    while lexeme_begin < len(program):
        max_forward: int = 0  # TODO: set it to 0
        final_token: Token | None = None

        forward, new_lines, token = ld.is_whitespace(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        # is_new_line, is_tab, whitespace_token = ld.is_whitespace(program[lexeme_begin:])
        # if whitespace_token is not None:
        #     if is_tab:
        #         lexeme_begin += 1
        #     else:
        #         lexeme_begin += 1
        #     whitespace_token.set_line(line)
        #     tokens.append(whitespace_token)
        #     if is_new_line:
        #         line += 1
        #     continue

        forward, token = ld.is_bool(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_break(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_char(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_continue(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_return(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_if(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_else(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_for(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_false(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_true(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_int(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_print(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_comment(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token
            new_lines = 1

        forward, token = ld.is_string(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_character(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_delimiter(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_bracket(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_curly_bracket(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_parenthesis(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_assignment(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_logical(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_relational(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_arithmatic(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_decimal(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_hex(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        forward, token = ld.is_id(program[lexeme_begin:])
        if token is not None and forward > max_forward:
            max_forward = forward
            final_token = token

        final_token.set_index(lexeme_begin)
        lexeme_begin += max_forward
        final_token.set_line(line)
        line += new_lines
        tokens.append(final_token)

    return tokens

# print(*tokenize(r"""
# (0x2355
# 0xfffff
# 123)
# """), sep="\n")
#
# print(*tokenize(r"""
# "\"helllo"
# int main() {
# // helsd;fks;dk;sldkf
#     int x = 2 + y -z  - 45;
#     return 0;
# }"""), sep="\n")

# print(*tokenize(r"""int test_function(int a, int b, bool c){
# 	// this is a function
# 	if (c == true){
# 		return a+b;
# 	}
# 	else {
# 		return a-b;
# 	}
# }
#
# int main(){
# 	bool add = true;
# 	char _assign1 = '=';
# 	char String_1[] = " + ";
# 	char String_2[] = " - ";
# 	for(int i = 0; i <= (+10 / 2); i = i + 1){
# 		for (int j = 0x0; j != (5 * -1)  ; j = j - 1){
# 			print(i);
# 			print(String_1);
# 			print(j);
# 			print(_assign1);
# 			print(test_function(i,j,add));
# 		}
# 	}
# 	add = false;
# 	for (int i = 0; !(i == +5); i = i + 1) {
# 		for (int j = 0x0; j >= -5; j = j - 1) {
# 			if((i % 4) == 0 || (i % 3) == 0)
# 				continue;
# 			if(j < -4 && i > 3)
# 				break;
# 			print(i);
# 			print(String_2);
# 			print(j);
# 			print(_assign1);
# 			print(test_function(i, j, add));
# 		}
# 	}
# 	print("this is\" a whole string no other token like '=' or 'else' or even \\\\comment should be recogized");
# 	char back = '\\';
# 	char quote = '\'';
# 	int _123 = 0XABCdef1230;
# }"""), sep="\n")

# print(*tokenize(r"""int test_function(int a, int b, bool c){
# 	// this is a function
# 	if (c == true){
# 		return a+b;
# 	}
# 	else {
# 		return a-b;
# 	}
# }
#
# int main(){
# 	bool add = true;
# 	char _assign1 = '=';
# 	char String_1[] = " + ";
# 	char String_2[] = " - ";
# 	for(int i = 0; i <= (+10 / 2); i = i + 1){
# 		for (int j = 0x0; j != (5 * -1)  ; j = j - 1){
# 			print(i);
# 			print(String_1);
# 			print(j);
# 			print(_assign1);
# 			print(test_function(i,j,add));
# 		}
# 	}
# 	add = false;
# 	for (int i = 0; !(i == +5); i = i + 1) {
# 		for (int j = 0x0; j >= -5; j = j - 1) {
# 			if((i % 4) == 0 || (i % 3) == 0)
# 				continue;
# 			if(j < -4 && i > 3)
# 				break;
# 			print(i);
# 			print(String_2);
# 			print(j);
# 			print(_assign1);
# 			print(test_function(i, j, add));
# 		}
# 	}
# 	print("this is\" a whole string no other token like '=' or 'else' or even \\\\comment should be recogized");
# 	char back = '\\';
# 	char quote = '\'';
# 	int _123 = 0XABCdef1230;
# }
# "\"" """), sep="\n")

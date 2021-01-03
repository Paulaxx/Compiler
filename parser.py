import ply.yacc as yacc
from lexer import tokens
import sys

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)


def p_program_declaration(p):
    'program : DECLARE declarations BEGIN commands END'
    pass


def p_program_begin(p):
    'program : BEGIN commands END'
    pass


def p_declarations_declarations_pidentifier(p):
    'declarations : declarations COMMA pidentifier'
    pass


def p_declarations_declarations_pidentifier_num(p):
    'declarations : declarations COMMA pidentifier LPAREN num COLON num'
    pass


def p_declarations_pidentifier(p):
    'declarations : pidentifier'
    pass


def p_declarations_pidentifier_num(p):
    'declarations : pidentifier LPAREN num COLON num RPAREN'
    pass


def p_commands_commands_command(p):
    'commands : commands command'
    pass


def p_commands_command(p):
    'commands : command'
    pass


def p_command_identifier_expression(p):
    'command : identifier ASSIGN expression SEMICOLON'
    pass


def p_command_if_else(p):
    'command : IF condition THEN commands ELSE commands ENDIF'
    pass


def p_command_if(p):
    'command : IF condition THEN commands ENDIF'
    pass


def p_command_while(p):
    'command : WHILE condition DO commands ENDWHILE'
    pass


def p_command_repeat_until(p):
    'command : REPEAT commands UNTIL condition SEMICOLON'
    pass


def p_command_for(p):
    'command : FOR pidentifier FROM value TO value DO commands ENDFOR'
    pass


def p_command_for_downto(p):
    'command : FOR pidentifier FROM value DOWNTO value DO commands ENDFOR'
    pass


def p_read(p):
    'command : READ identifier SEMICOLON'
    pass


def p_write(p):
    'command : WRITE value SEMICOLON'
    pass


def p_expression_value(p):
    'expression : value'
    pass


def p_expression_plus(p):
    'expression : value PLUS value'
    pass


def p_expression_minus(p):
    'expression : value MINUS value'
    pass


def p_expression_times(p):
    'expression : value TIMES value'
    pass


def p_expression_divide(p):
    'expression : value DIVIDE value'
    pass


def p_expression_modulo(p):
    'expression : value MODULO value'
    pass


def p_condition_equal(p):
    'condition : value EQUALS value'
    pass


def p_condition_not_equal(p):
    'condition : value NOTEQUALS value'
    pass


def p_condition_lesser(p):
    'condition : value LESSER value'
    pass


def p_condition_greater(p):
    'condition : value GREATER value'
    pass


def p_condition_leq(p):
    'condition : value LEQ value'
    pass


def p_condition_geq(p):
    'condition : value GEQ value'
    pass


def p_value_num(p):
    'value : num'
    pass


def p_value_identifier(p):
    'value : identifier'
    pass


def p_identifier_pidentifier(p):
    'identifier : pidentifier'
    pass


def p_identifier_pidentifier_pidentifier(p):
    'identifier : pidentifier LPAREN pidentifier RPAREN'
    pass


def p_identifier_pidentifier_num(p):
    'identifier : pidentifier LPAREN num RPAREN'
    pass

def p_error(p):
    pass


def main():
    inputFile = sys.argv[1]
    # outFile = sys.argv[2]
    parser = yacc.yacc()
    with open(inputFile, "r") as file:
        parser.parse(file.read())


if __name__ == "__main__":
    main()
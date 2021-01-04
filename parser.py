import ply.yacc as yacc
from lexer import tokens
import sys
from SymbolTable import *
from MachineCode import *
from Expression import *

symbol_table = SymbolTable()
code = MachineCode();

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
    symbol_table.add_variable(p[3])


def p_declarations_declarations_pidentifier_num(p):
    'declarations : declarations COMMA pidentifier LPAREN num COLON num RPAREN'
    symbol_table.add_table(p[3], p[5], p[7])


def p_declarations_pidentifier(p):
    'declarations : pidentifier'
    symbol_table.add_variable(p[1])


def p_declarations_pidentifier_num(p):
    'declarations : pidentifier LPAREN num COLON num RPAREN'
    symbol_table.add_table(p[1], p[3], p[5])


def p_commands_commands_command(p):
    'commands : commands command'
    pass


def p_commands_command(p):
    'commands : command'
    pass


def p_command_identifier_expression(p):
    'command : identifier ASSIGN expression SEMICOLON'
    code.assign(p[3].register, p[1])


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
    code.read(p[2])
    p[2][0]['is_in_memory'] = 1
    p[2][0]['value'] = 0


def p_write(p):
    'command : WRITE value SEMICOLON'
    code.write(p[2])
    if isinstance(p[2], list):
        p[2] = p[2][0]
    p[2]['is_in_memory'] = 1


def p_expression_value(p):
    'expression : value'
    reg = code.expression_1(p[1])
    p[0] = Expression(reg)


def p_expression_plus(p):
    'expression : value PLUS value'
    reg = code.expression_plus_minus(p[1], p[3], p[2])
    p[0] = Expression(reg)


def p_expression_minus(p):
    'expression : value MINUS value'
    reg = code.expression_plus_minus(p[1], p[3], p[2])
    p[0] = Expression(reg)


def p_expression_times(p):
    'expression : value TIMES value'
    reg = code.expression_times(p[1], p[3])
    p[0] = Expression(reg)


def p_expression_divide(p):
    'expression : value DIVIDE value'
    reg = code.expression_divide(p[1], p[3])
    p[0] = Expression(reg)


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
    p[0] = symbol_table.get_num(p[1])


def p_value_identifier(p):
    'value : identifier'
    p[0] = p[1]


def p_identifier_pidentifier(p):
    'identifier : pidentifier'
    p[0] = symbol_table.get_variable(p[1])


def p_identifier_pidentifier_pidentifier(p):
    'identifier : pidentifier LPAREN pidentifier RPAREN'
    p[0] = symbol_table.get_table_on_position_pidentifier(p[1], p[3])


def p_identifier_pidentifier_num(p):
    'identifier : pidentifier LPAREN num RPAREN'
    p[0] = symbol_table.get_table_on_position_num(p[1], p[3])


def p_error(p):
    if p:
        print("Syntax error at token", p.type)
    else:
        print("Syntax error at EOF")
    exit(5)


def main():
    inputFile = "test.imp"
    # outFile = sys.argv[2]
    parser = yacc.yacc()
    with open(inputFile, "r") as file:
        parser.parse(file.read())
    c=0
    for i in code.code:
        print(c, i)
        c += 1
    for i in symbol_table.table:
        print(i)


if __name__ == "__main__":
    main()
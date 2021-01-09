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


def p_program_begin(p):
    'program : BEGIN commands END'


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
    if p[1] is None:
        p[1] = Command(0)
    p[1] = Command(p[1].counter + p[2].counter)
    p[0] = p[1]


def p_commands_command(p):
    'commands : command'
    p[0] = Command(p[1].counter)


def p_command_identifier_expression(p):
    'command : identifier ASSIGN expression SEMICOLON'
    s1 = len(code.code)
    code.assign(p[3].register, p[1])
    if isinstance(p[1], list):
        p[1][0]['value'] = 0
        p[1][0]['is_in_memory'] = 1
    else:
        p[1]['value'] = 0
        p[1]['is_in_memory'] = 1
    s2 = len(code.code)
    p[0] = Command(s2 - s1 + p[3].counter)


def p_command_if_else(p):
    'command : IF condition THEN commands ELSE commands ENDIF'
    s1 = len(code.code)
    code.if_else(p[2].jump, p[4].counter, p[6].counter)
    s2 = len(code.code)
    p[0] = Command(s2 - s1 + p[2].counter + p[4].counter + p[6].counter)


def p_command_if(p):
    'command : IF condition THEN commands ENDIF'
    s1 = len(code.code)
    code.just_if(p[2].jump, s1)
    s2 = len(code.code)
    p[0] = Command(s2 - s1 + p[2].counter + p[4].counter)


def p_command_while(p):
    'command : WHILE condition DO commands ENDWHILE'
    s1 = len(code.code)
    code.while_command(s1, p[2].jump, p[2].start)
    s2 = len(code.code)
    p[0] = Command(s2 - s1 + p[2].counter + p[4].counter)


def p_command_repeat_until(p):
    'command : REPEAT commands UNTIL condition SEMICOLON'
    s1 = len(code.code)
    code.delete_alt_orders(p[4].counter)
    s11 = len(code.code)
    if p[4].sign == '=':
        sign = '!='
    elif p[4].sign == '!=':
        sign = '='
    elif p[4].sign == '>':
        sign = '<='
    elif p[4].sign == '<':
        sign = '>='
    elif p[4].sign == '>=':
        sign = '<'
    else:
        sign = '>'
    start, jump = code.condition_1(p[4].value1, p[4].value2, sign)
    s22 = len(code.code)
    code.repeat_until(p[2].counter + s22-s11, jump)
    s2 = len(code.code)
    p[0] = Command(s2 - s1 + p[2].counter + p[4].counter)


def p_command_for(p):
    'command : FOR pidentifier FROM value TO value DO commands ENDFOR'
    s1 = len(code.code)
    s2 = len(code.code)
    p[0] = Command(s2 - s1)


def p_command_for_downto(p):
    'command : FOR pidentifier FROM value DOWNTO value DO commands ENDFOR'
    s1 = len(code.code)
    s2 = len(code.code)
    p[0] = Command(s2 - s1)


def p_read(p):
    'command : READ identifier SEMICOLON'
    s1 = len(code.code)
    code.read(p[2])
    if isinstance(p[2], list):
        p[2] = p[2][0]
    p[2]['is_in_memory'] = 1
    p[2]['value'] = 0  # zainicjalizowana
    # p[2]['is_in_memory'] = 1
    # p[2]['value'] = 0
    s2 = len(code.code)
    p[0] = Command(s2 - s1)


def p_write(p):
    'command : WRITE value SEMICOLON'
    s1 = len(code.code)
    code.write(p[2])
    if isinstance(p[2], list):
        p[2] = p[2][0]
    p[2]['is_in_memory'] = 1
    s2 = len(code.code)
    p[0] = Command(s2 - s1)


def p_expression_value(p):
    'expression : value'
    s1 = len(code.code)
    reg = code.expression_1(p[1])
    s2 = len(code.code)
    p[0] = Expression(reg, s2 - s1)


def p_expression_plus(p):
    'expression : value PLUS value'
    s1 = len(code.code)
    reg = code.expression_plus_minus(p[1], p[3], p[2])
    s2 = len(code.code)
    p[0] = Expression(reg, s2 - s1)


def p_expression_minus(p):
    'expression : value MINUS value'
    s1 = len(code.code)
    reg = code.expression_plus_minus(p[1], p[3], p[2])
    s2 = len(code.code)
    p[0] = Expression(reg, s2 - s1)


def p_expression_times(p):
    'expression : value TIMES value'
    s1 = len(code.code)
    reg = code.expression_times(p[1], p[3])
    s2 = len(code.code)
    p[0] = Expression(reg, s2 - s1)


def p_expression_divide(p):
    'expression : value DIVIDE value'
    s1 = len(code.code)
    reg = code.expression_divide(p[1], p[3])
    s2 = len(code.code)
    p[0] = Expression(reg, s2 - s1)


def p_expression_modulo(p):
    'expression : value MODULO value'
    s1 = len(code.code)
    reg = code.expression_modulo(p[1], p[3])
    s2 = len(code.code)
    p[0] = Expression(reg, s2 - s1)


def p_condition(p):
    """
    condition : value EQUALS value
                | value NOTEQUALS value
                | value LESSER value
                | value GREATER value
                | value LEQ value
                | value GEQ value
    """
    s1 = len(code.code)
    start, jump = code.condition_1(p[1], p[3], p[2])
    s2 = len(code.code)
    p[0] = Condition(start, jump, s2 - s1, p[1], p[3], p[2])


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
    # inputFile = sys.argv[1]
    inputFile = "test.imp"
    # outputFile = sys.argv[2]
    outputFile = "out.mr"
    parser = yacc.yacc()
    with open(inputFile, "r") as file:
        parser.parse(file.read())

    """
    for i in symbol_table.table:
        print(i)
    c=0
    for i in code.code:
        print(c, i)
        c += 1
    """
    with open(outputFile, "w") as file:
        for i in code.code:
            file.write(i['com'] + " " + str(i['arg1']) + " " + str(i['arg2']) + '\n')
        file.write("HALT")


if __name__ == "__main__":
    main()

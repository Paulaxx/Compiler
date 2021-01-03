import ply.lex as lex

tokens = (
        'DECLARE', 'BEGIN', 'END',
        'THEN', 'ELSE', 'ENDIF', 'IF',
        'WHILE', 'ENDWHILE', 'DO',
        'REPEAT', 'UNTIL',
        'FROM', 'DOWNTO', 'TO', 'ENDFOR', 'FOR',
        'READ', 'WRITE',
        'LPAREN', 'RPAREN',
        'SEMICOLON', 'COLON', 'COMMA',
        'pidentifier', 'num',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
        'EQUALS', 'NOTEQUALS', 'LESSER', 'GREATER',
        'LEQ', 'GEQ',
        'ASSIGN'
)

t_ignore = ' \t'

t_DECLARE = r'DECLARE'
t_BEGIN = r'BEGIN'
t_END = r'END'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_ENDIF = r'ENDIF'
t_IF = r'IF'
t_WHILE = r'WHILE'
t_ENDWHILE = r'ENDWHILE'
t_DO = r'DO'
t_REPEAT = r'REPEAT'
t_UNTIL = r'UNTIL'
t_FROM = r'FROM'
t_DOWNTO = r'DOWNTO'
t_TO = r'TO'
t_ENDFOR = r'ENDFOR'
t_FOR = r'FOR'
t_READ = r'READ'
t_WRITE = r'WRITE'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_MODULO = r'\%'
t_EQUALS = r'\='
t_NOTEQUALS= r'!='
t_LESSER= r'<'
t_GREATER = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_ASSIGN = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_pidentifier = r'[_a-z]+'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("Niepoprawny symbol", t.value[0], "x")



lexer = lex.lex()
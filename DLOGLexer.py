import ply.lex as lex

reserved_keywords = {
    'not': 'NOT'
}

tokens =  [
    'NUM',
    'ID',
    'EQ',
    'DOT',
    'COMMA',
    'LPRN',
    'RPRN'
] + list(reserved_keywords.values())

t_LPRN = r'\('
t_RPRN = r'\)'
t_COMMA = r','
t_DOT = r'\.'
t_EQ = r':-'


def t_NOT(t):
    r'[nN][oO][tT]'
    return t


def t_ID(t):
    r'[a-z]+[0-9]*'
    t.type = 'ID'
    return t


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t




# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'


def t_error(t):
    print(f"Illegal character {t.value[0]}")
    raise Exception('LEXER ERROR')


lexer = lex.lex()

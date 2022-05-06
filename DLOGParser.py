from DLOGLexer import tokens
from ply import yacc

class Container:
    def __init__(self):
        self.lhs = set()
        self.rhs = set()

    def lhs_add(self, st):
        if isinstance(st, str):
            self.lhs.add(st)

    def rhs_add(self, st):
        if isinstance(st, str):
            self.rhs.add(st)
    
    def rhs_remove(self, st):
        self.rhs.remove(st)

    def check(self):
        return self.rhs.__eq__(self.lhs)
    
    # Debug
    def print(self):
        print(f'LHS = {self.lhs}, Len = {len(self.lhs)}')
        print(f'RHS = {self.rhs}, Len = {len(self.rhs)}')

    def clean(self):
        self.rhs.clear()
        self.lhs.clear()

container = Container()

def p_dlog_start(p):
    '''dlogStart : dlog DOT'''
    # container.print() # Debug
    p[0] = container.check()
    container.clean()

def p_dlog(p):
    '''dlog : lhs EQ rhs'''

def p_lhs(p):
    '''lhs : lhs_formula'''

def p_formula(p):
    '''lhs_formula : ID LPRN list1 RPRN'''

def p_lhs_formula_list(p):
    '''list1 : list1 COMMA ID'''
    container.lhs_add(p[3].upper())

def p_lhs_formula_list_base(p):
    '''list1 : ID'''
    container.lhs_add(p[1].upper())

def p_rhs(p):
    '''rhs : rhs COMMA atomic'''

def p_rhs_base(p):
    '''rhs : atomic'''

def p_atomic_types(p):
    '''atomic : positive
              | negation'''

def p_atomic(p):
    '''positive : rhs_formula'''
    for i in p[1]:
        if isinstance(i, str):
            container.rhs_add(i)

def p_rhs_formula_negation(p):
    '''negation : NOT rhs_formula'''
    for i in p[2]:
        if isinstance(i, str) and i in container.rhs:
            container.rhs_remove(i)

def p_rhs_formula(p):
    '''rhs_formula : ID LPRN list2 RPRN'''
    p[0] = p[3]

def p_rhs_list2(p):
    '''list2 : list2 COMMA ID
             | list2 COMMA NUM'''
    p[0] = {p[3].upper() if isinstance(p[3], str) else p[3]}.union(p[1])

def p_rhs_list2_base(p):
    '''list2 : ID
             | NUM'''
    p[0] = {p[1].upper() if isinstance(p[1], str) else p[1]}


def p_error(p):
    pass

parser = yacc.yacc()
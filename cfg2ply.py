import sys


def convert(fname):
    with open(fname) as f:
        project = f.readline().strip()
        print('import ply.yacc as yacc')
        print('from '+project+'Lexer import tokens\n')
        rules = {}
        while True:
            line = f.readline().strip()
            if not line:
                break
            # print(line)
            xs = line.split(':')
            lhs = xs[0].strip()
            rhs = xs[1].strip()
            if lhs in rules:
                rules[lhs].append(rhs)
            else:
                rules[lhs] = [rhs]
        # print(rules)
        for lhs in rules:
            for (i, rhs) in enumerate(rules[lhs]):
                print('def p_'+lhs+'_'+str(i)+'(p):')
                print('  \''+lhs+' : '+rhs+'\'')
                print('  p[0] =\n')
        print('def p_error(p):')
        print('  print("Syntax error in input!")\n')
        print('parser = yacc.yacc()')


convert(sys.argv[1])

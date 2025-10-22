import ply.lex as lex
import ply.yacc as yacc

tokens = ('ARROW', 'BAR', 'TERM', 'NONTERM', 'NEWLINE')

t_ARROW = r'->'
t_BAR = r'\|'

## terminals are in single quotes
def t_TERM(t):
    r'\'[^\']*\''
    t.value = t.value.strip("'")
    return t

## anything that is a valid python variable can be used as a non terminal
def t_NONTERM(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

lexer = lex.lex()

def p_grammar(p):
    '''grammar : rules'''
    p[0] = p[1]

def p_rules_multiple(p):
    '''rules : rules NEWLINE rule'''
    p[0] = p[1]
    
    ## prevent the overwiriting of rules
    for lhs, rhs in p[3].items():
        if lhs in p[0]:
            p[0][lhs].extend(rhs)
        else:
            p[0][lhs] = rhs

def p_rules_single(p):
    '''rules : rule
             | NEWLINE rule'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_rule(p):
    '''rule : NONTERM ARROW productions'''
    lhs = p[1]
    rhs = p[3]
    p[0] = {lhs: rhs}

def p_productions_multiple(p):
    '''productions : productions BAR production'''
    p[0] = p[1]
    p[0].append(p[3])

def p_productions_single(p):
    '''productions : production'''
    p[0] = [p[1]]

def p_production_symbols(p):
    '''production : symbol_list'''
    p[0] = p[1]

def p_symbol_list_multiple(p):
    '''symbol_list : symbol_list TERM
                   | symbol_list NONTERM'''
    p[0] = p[1]
    p[0].append(p[2])

def p_symbol_list_single(p):
    '''symbol_list : TERM
                   | NONTERM'''
    p[0] = [p[1]]

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

'''print("Enter your grammar (press Enter on an empty line to finish):")
lines = []
while True:
    line = input()
    if line.strip() == "":  ## empty line
        break
    lines.append(line)

data = "\n".join(lines).strip()

result = parser.parse(data, lexer=lexer)
print(result)'''
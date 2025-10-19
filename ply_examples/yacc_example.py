# Yacc example
# from: https://www.dabeaz.com/ply/ply.html
import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from calclex import tokens

# In this example, each grammar rule is defined by a Python function
# where the docstring to that function contains the appropriate
# context-free grammar specification. The statements that make up the
# function body implement the semantic actions of the rule.

# Each function accepts a single argument p that is a sequence
# containing the values of each grammar symbol in the corresponding rule.
# The values of p[i] are mapped to grammar symbols as shown here:
#     def p_expression_plus(p):
#         'expression : expression PLUS term'
#         #   ^            ^        ^    ^
#         #  p[0]         p[1]     p[2] p[3]

#         p[0] = p[1] + p[3]


def p_expression_plus(p):
    "expression : expression PLUS term"
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    "expression : expression MINUS term"
    p[0] = p[1] - p[3]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


def p_term_times(p):
    "term : term TIMES factor"
    p[0] = p[1] * p[3]


def p_term_div(p):
    "term : term DIVIDE factor"
    p[0] = p[1] / p[3]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : NUMBER"
    p[0] = p[1]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

print("\n------CALC EXAMPLE-------")
while True:
    
    try:
        s = input("calc > ")
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)

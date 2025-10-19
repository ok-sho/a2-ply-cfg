# ------------------------------------------------------------
# cfg2.py
#
# tokenizing and parsing ambiguous CFG from Sipser exercise 2.3
# ------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# ------------------ LEXER -----------------

# List of token names. This is always required; used to perform validation checks
# tokens list is also used by yacc.py to identify terminals
tokens = (
    "A",
    "B",
)

# Regular expression rules for simple tokens
t_A = r"a"
t_B = r"b"

# A string containing ignored characters (spaces and tabs)
t_ignore = " \t\n"
# t_ignore_COMMENT = r'\#.*'

# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

# Compute column.
#     input is the input text string
#     token is a token instance
# Since column information is often only useful in the context of error handling, calculating the column position can be performed when needed as opposed to doing it for each token.
def find_column(input, token):
    line_start = input.rfind("\n", 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# ------------ PARSER ----------------
# Grammar rules

def p_R_XRX(p):
    "R : X R X"
    p[0] = p[1] + p[2] + p[3]


def p_R_S(p):
    "R : S"
    p[0] = p[1]
    print("R -> S")


def p_S_aTb(p):
    "S : A T B"
    p[0] = "a" + p[2] + "b"
    print("S -> aTb")


def p_S_bTa(p):
    "S : B T A"
    p[0] = "b" + p[2] + "a"
    print("S -> bTa")


def p_T_XTX(p):
    "T : X T X"
    p[0] = p[1] + p[2] + p[3]
    print("T -> XTX")


def p_T_X(p):
    "T : X"
    p[0] = p[1]
    print("T -> X")


def p_T_epsilon(p):
    "T :"
    p[0] = ""
    print("T -> ε")


def p_X_a(p):
    'X : A'
    p[0] = 'a'
    print("X -> a")

def p_X_b(p):
    'X : B'
    p[0] = 'b'
    print("X -> b")


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc(debug=True)


# -------- RUN --------------
if __name__ == "__main__":

    # Test it out
    data = """
    abba
    """

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        # lexer.token returns instances of LexToken
        # with attributes tok.type, tok.value, tok.lineno, and tok.lexpos
        #  If you need to store multiple values on a token, assign a tuple, dictionary, or instance to value.
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

    # L(G) is the list of all strings over a and b that are not palindromes
    test_strings = [
        "ab",  # accept
        "ba",  # accept
        "aabb",  # accept
        "abba",  # reject
        "baba",  # accept
        "aaabbb",  # accept
        "aabab",  # accept
        "babbab",  # reject
        "aabaabaa",  # reject
        "abcd",  # reject (invalid chars)
        "aaa",  # reject (not matching S pattern)
    ]

    print("\nGrammar Rules:")
    print("  R -> XRX | S")
    print("  S -> aTb | bTa")
    print("  T -> XTX | X | ε")
    print("  X -> a | b")

    for test in test_strings:
        print(f"\n--- Testing: '{test}' ---")
        result = parser.parse(test, lexer=lexer)
        if result:
            print(f"Accepted")
        else:
            print(f"Rejected")

# or do it interactively:

# while True:
#    try:
#        s = input('string > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)

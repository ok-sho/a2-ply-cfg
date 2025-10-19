# ------------------------------------------------------------
# cfg1.py
#
# tokenizing and parsing a simple CFG, G_1 from Sipser text 2.1
# ------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc

# ------------------ LEXER -----------------

# List of token names. This is always required; used to perform validation checks
# tokens list is also used by yacc.py to identify terminals
tokens = (
    "ZERO",
    "ONE",
    "HASH",
)

# Regular expression rules for simple tokens
t_ZERO = r"0"
t_ONE = r"1"
t_HASH = r"\#"

# A string containing ignored characters (spaces and tabs)
t_ignore = " \t\n"
# t_ignore_COMMENT = r'\#.*'

# A regular expression rule with some action code
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t


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

# Each function accepts a single argument p that is a sequence containing the values of each grammar symbol in the corresponding rule. The values of p[i] are mapped to grammar symbols as shown here:

#     def p_expression_plus(p):
#         'expression : expression PLUS term'
#         #   ^            ^        ^    ^
#         #  p[0]         p[1]     p[2] p[3]

#         p[0] = p[1] + p[3]


# Grammar rules
def p_A_0A1(p):
    "A : ZERO A ONE"
    # p[0]:p[1] p[2] p[3]
    p[0] = "0" + p[2] + "1"
    print("A -> 0A1")


def p_A_B(p):
    "A : B"
    p[0] = p[1]
    print("A -> B")


def p_B_HASH(p):
    "B : HASH"
    p[0] = p[1]
    print("B -> #")


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()


# -------- RUN --------------
if __name__ == "__main__":
    
    print("\n\n---------CFG1---------\n")
    print("  A -> 0A1")
    print("  A -> B")
    print("  B -> #\n")


    # # Test it out
    # data = """
    # 0#1
    # """

    # # Give the lexer some input
    # lexer.input(data)

    # # Tokenize
    # while True:
    #     # lexer.token returns instances of LexToken
    #     # with attributes tok.type, tok.value, tok.lineno, and tok.lexpos
    #     #  If you need to store multiple values on a token, assign a tuple, dictionary, or instance to value.
    #     tok = lexer.token()
    #     if not tok:
    #         break  # No more input
    #     print(tok)

    test_strings = [
        "#",  # accept, B -> H
        "0#1",  # accept, A -> 0A1 -> 0B1 -> 0H1
        "00#11",  # accept, A -> 0A1 -> 00A11 -> 00B11 -> 00H11
        "000#111",  # accept
        "0#11",  # reject, 0s != 1s
        "00#1",  # reject, 0s != 1s
    ]

    for test in test_strings:
        print(f"\n--- Test string: '{test}' ---")
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

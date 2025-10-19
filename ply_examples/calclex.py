# from: https://www.dabeaz.com/ply/ply.html
# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names. This is always required; used to perform validation checks
# tokens list is also used by yacc.py to identify terminals
tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
)

# To handle reserved words, you should write a single rule to match an identifier 
# and do a special name lookup in a function like this:

#    reserved = {
#       'if' : 'IF',
#       'then' : 'THEN',
#       'else' : 'ELSE',
#       'while' : 'WHILE',
#       ...
#    }

#    tokens = ['LPAREN','RPAREN',...,'ID'] + list(reserved.values())

# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]*'
#     t.type = reserved.get(t.value,'ID')    # Check for reserved words
#     return t

# Regular expression rules for simple tokens
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"


# A regular expression rule with some action code
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Compute column.
#     input is the input text string
#     token is a token instance
# Since column information is often only useful in the context of error handling, 
# calculating the column position can be performed when needed as opposed to 
# doing it for each token.
def find_column(input, token):
    line_start = input.rfind("\n", 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"
t_ignore_COMMENT = r"\#.*"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Lex example
# from: https://www.dabeaz.com/ply/ply.html

from calclex import lexer

# The lexer requires input to be supplied as a single input string. 
# This means that the lexer can't be used with streaming data 
# such as open files or sockets.
data = """
3 + 4 * 10
  + -20 *2
"""

# Give the lexer some input
lexer.input(data)

print("\n------LEXTOKEN EXAMPLE-------\n")
print("input: \n", data)
print("\nLexToken(type, value, lineno, lexpos)\n")

# Tokenize
while True:
    # lexer.token returns instances of LexToken
    # with attributes tok.type, tok.value, tok.lineno, and tok.lexpos
    #  If you need to store multiple values on a token, assign a tuple, dictionary, or instance to value.
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

# How to set up
1. set up venv (Python 3.13.0)
2. `pip install -r requirements.txt`
3. copy `ply` directory from [creator's github](https://github.com/dabeaz/ply/tree/master) into into `.venv/lib/`. (github readme states PLY is not distributed through a package manager)

# Contents
1. `ply_examples/` contains example code from [PLY Docs](https://www.dabeaz.com/ply/ply.html)
   1. `calclex.py` is not run directly, but is used for the next two:
   2. `lex_example.py` demonstrates lex tokenization
   3. `yacc_example.py` demonstrates yacc parsing
1. `cfg1.py` is CFG G_1 from Sipser 2.1. Unambiguous; works!
2. `cfg2.py` is from Sipser Exercise 2.3. Ambiguous; broken, with many errors! Shows `parser.out`, shift/reduce and reduce/reduce conflicts
3. `tock_ex.py` shows tock package in action and how it works with the ambiguous grammar from `cfg2.py` and converts it to a PDA with graph.
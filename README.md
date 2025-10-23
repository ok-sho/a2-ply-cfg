# References

Beazley, D. M. (n.d.). _PLY (Python Lex-Yacc)_. Dabeaz. Retrieved Oct 18, 2025, from https://www.dabeaz.com/ply/ply.html

Campbell, R. (2025). _Week 5: Sec 2.1 Context-Free Grammars_ [PDF Lecture Slides]. Retrieved from https://brightspace.ufv.ca/content/enforced/21563-202509-91633/Week5/Sec2_1.pdf

Campbell, R. (2025). _Week 6: Sec 2.2 Pushdown Automata_ [PDF Lecture Slides]. Retrieved 
from https://brightspace.ufv.ca/content/enforced/21563-202509-91633/Week6/Sec2_2.pdf

Levine, J. R., Mason, T., & Brown, D. (1992). _Lex & Yacc_. Retrieved from https://archive.org/details/lexyacc0000levi/

Sipser, M. (2013). _Introduction to the Theory of Computation_ (3rd ed.). Cengage Learning

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

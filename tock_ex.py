from tock import *
from graphviz import Source

g1 = Grammar.from_lines(
    [
        "R -> X R X",
        "R -> S",
        "S -> a T b",
        "S -> b T a",
        "T -> X T X",
        "T -> X",
        "T -> ε",
        "X -> a",
        "X -> b",
    ]
)

p1 = from_grammar(g1)
to_graph(p1)

write_dot(p1, "graph")
path = "graph"
s = Source.from_file(path)
s.view()

if __name__ == '__main__':
    print("-------CFG------")
    print(g1)
    run(p1, "a a a b", show_stack=10).shortest_path()
    s.view()

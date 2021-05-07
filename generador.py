from yard import Yard
from CPMP import CPMP_Node
import dtls
import pandas as pd

# n -> iterations
# h -> height
# s -> stacks
# e -> empty rows
# a,b -> values range


def generate_dataset(filename, n, h, s, e, a, b, compact=False, norm=False, elev=False):
    states = []
    init_moves = []
    final_moves = []
    for i in range(n):
        yard = Yard(s, h, e, a, b)
        node = CPMP_Node(yard, None)
        result = dtls.dlts_lds(node)
        result.get_data(states, init_moves, final_moves, compact, norm, elev)
    df = pd.DataFrame(states)
    df.insert(0, column="init_move", value=pd.DataFrame(init_moves))
    df.insert(0, column="final_move", value=pd.DataFrame(final_moves))
    df.to_csv(filename)


def load_df(filename):
    pass


#generate_dataset("train_df.csv", 4000, 3, 3, 1, 1, 9, True, True, True)
#generate_dataset("test_df.csv", 3000, 3, 3, 1, 1, 9, True, True, True)
load_df('train_df.csv')


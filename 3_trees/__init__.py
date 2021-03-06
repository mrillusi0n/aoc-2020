from math import prod
from itertools import starmap
from functools import partial

def parse_input(text):
    return text.split()

def get_tree_count(geo, step_right, step_down, cols):
    return sum(
        int(row[(step_right * i) % cols])
        for i, row in enumerate(
            list(map(lambda x: x.replace('#', '1').replace('.', '0'),
                     geo))[step_down::step_down], start=1))

def solve(geo, parts):
    solvers = {
        1: get_tree_count(geo, 3, 1, len(geo[0])),
        2: prod(starmap(partial(get_tree_count, geo, cols=len(geo[0])),
                        ((3, 1), (1, 1), (5, 1), (7, 1), (1, 2)))),
    }

    return list(map(solvers.get, parts))

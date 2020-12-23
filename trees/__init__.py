from math import prod
from itertools import starmap
from functools import partial

def read_input(file):
    return list(map(str.rstrip, file.readlines()))

def get_tree_count(geo, step_right, step_down, cols):
    return sum(int(row[(step_right * i) % cols]) for i, row in enumerate(list(map(lambda x: x.replace('#', '1').replace('.', '0'), geo))[step_down::step_down], start=1))

def solve(geo):
    return prod(starmap(partial(get_tree_count, geo, cols=len(geo[0])), ((3, 1), (1, 1), (5, 1), (7, 1), (1, 2))))


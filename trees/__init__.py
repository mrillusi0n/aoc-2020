from math import prod

def read_input(file):
    return list(map(lambda x: x.rstrip(), file.readlines()))

def get_tree_count(geo, step_right, step_down, cols):
    return sum(int(row[(step_right * i) % cols]) for i, row in enumerate(list(map(lambda x: x.replace('#', '1').replace('.', '0'), geo))[step_down::step_down], start=1))

def solve(geo):
    product = 1
    cols = len(geo[0])

    for pair in ((3, 1), (1, 1), (5, 1), (7, 1), (1, 2)):
        product *= get_tree_count(geo, *pair, cols)

    return product


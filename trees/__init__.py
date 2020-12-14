def get_tree_count(geo, step_right, step_down):
    trees = 0
    cols = len(geo[0])

    for i, row in enumerate(geo[::step_down]):
        trees += 1 if row[(i * step_right) % cols] == '#' else 0

    return trees

def solve(geo):
    product = 1

    for pair in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        product *= get_tree_count(geo, *pair)

    return product


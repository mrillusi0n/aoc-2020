def solve(geo):
    trees = 0
    cols = len(geo[0])
    start = 1

    for i, row in enumerate(geo):
        trees += 1 if row[(i * 3) % cols] == '#' else 0


    return trees


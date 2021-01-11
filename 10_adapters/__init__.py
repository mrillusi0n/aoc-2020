from math import prod

def read_input(f):
    return list(map(int, map(str.rstrip, f.readlines())))

def solve(data):
    max_jolts = max(data) + 3
    curr_jolts = 0
    res = []
    three_fives = {3: 0, 1: 0}

    for adapter in sorted(data) + [max_jolts]:
        if (d := adapter - curr_jolts) <= 3:
            res.append(adapter)
            curr_jolts = adapter
            three_fives[d] += 1

    return prod(three_fives.values())

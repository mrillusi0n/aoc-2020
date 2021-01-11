from functools import reduce
import operator

def get_yes_count(answers):
    return sum(map(lambda x: len(set(''.join(x))), answers))

def get_universal_answer(group):
    return reduce(operator.and_, group)

def solve(answers):
    return sum(map(lambda x: len(get_universal_answer(list(map(set, x)))), answers))

def read_input(file):
    with open(file) as f:
        return list(map(lambda x: x.split(), f.read().split('\n' * 2)))


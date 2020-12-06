def solve(answers):
    return sum(map(lambda x: len(set(''.join(x))), answers))



def read_input(file):
    with open(file) as f:
        return list(map(lambda x: x.split(), f.read().split('\n' * 2)))


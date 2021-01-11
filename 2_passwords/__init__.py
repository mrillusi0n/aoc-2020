from collections import Counter

def parse_input(text):
    return text.strip().split('\n')

def is_valid(p):
    constraint, password = p.split(': ')
    bounds, c = constraint.split()
    low, high = map(int, bounds.split('-'))

    freq = Counter(password)

    return low <= freq[c] <= high

def is_still_valid(p):
    constraint, password = p.split(': ')
    bounds, c = constraint.split()
    left, right = map(int, bounds.split('-'))

    res = (password[left-1] == c) + (password[right-1] == c)

    return 0 < res <= 1

def solve(passwords, parts):
    solvers = {
        1: len(list(filter(is_valid, passwords))),
        2: len(list(filter(is_still_valid, passwords))),
    }

    return list(map(solvers.get, parts))

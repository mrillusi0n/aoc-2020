def parse_input(text):
    return list(map(int, text.split()))

def get_two_years(years):
    years_set = set(years)

    for year in years_set:
        if (y := 2020 - year) in years_set:
            return y * year

def get_three_years(years):
    years_set = set(years)

    for a in years_set:
        for b in years_set - {a}:
            for c in years_set - {b}:
                if c == 2020 - a - b:
                    return a * b * c

def solve(data, parts):
    solvers = {
        1: get_two_years(data),
        2: get_three_years(data),
    }

    return list(map(solvers.get, parts))

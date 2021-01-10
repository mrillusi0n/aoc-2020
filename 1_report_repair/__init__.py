def parse_input(text):
    return list(map(int, text.split()))

def get_two_years(years):
    years_set = set(years)

    for year in years_set:
        if (y := 2020 - year) in years_set:
            return y * year

def get_three_years(years):
    pass

def solve(years):
    return get_two_years(years)

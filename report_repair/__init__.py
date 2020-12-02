def solve(years):
    years_set = set(years)

    for x in years_set:
        for y in years_set:
            if x + y > 2020:
                continue
            if (z := abs(x + y - 2020)) in years_set:
                return x * y * z

    return 'No pair found!'


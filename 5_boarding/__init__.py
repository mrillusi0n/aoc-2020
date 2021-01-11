def get_seat_id(space):
    row_bits = ['0'] * 7
    col_bits = ['0'] * 3

    for i, pos in enumerate(space[:7]):
        row_bits[i] = '1' if pos == 'B' else '0'

    for i, pos in enumerate(space[7:]):
        col_bits[i] = '1' if pos == 'R' else '0'

    return int(''.join(row_bits), 2) * 8 + int(''.join(col_bits), 2)

def get_natural_sum(n):
    return n * (n + 1) // 2

def solve(seats):
    seat_ids = list(map(get_seat_id, seats))
    return get_natural_sum(max(seat_ids)) - get_natural_sum(min(seat_ids) - 1) - sum(seat_ids)

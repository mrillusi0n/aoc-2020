from math import prod

def read_input(f):
    min_time, schedule = f.read().rstrip().split('\n')

    return int(min_time), schedule

def get_waiting_time(min_time, schedule):
    return prod(min(map(lambda b: (b, -min_time % b), map(int, filter(lambda x: x != 'x', schedule.split(',')))), key=lambda x: x[1]))

def solve(data):
    return get_waiting_time(*data)

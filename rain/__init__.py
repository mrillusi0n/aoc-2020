def read_input(file):
    return list(map(lambda x: x.rstrip(), file.readlines()))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.directions = [self.move_east, self.move_south, self.move_west, self.move_north]
        self.current_dir = 0

    def turn_left(self, step):
        self.current_dir = (self.current_dir - step // 90) % 4
        self.move = self.directions[self.current_dir]

    def turn_right(self, step):
        self.current_dir = (self.current_dir + step // 90) % 4
        self.move = self.directions[self.current_dir]

    def move_east(self, val):
        self.x += val

    def move_south(self, val):
        self.y += val

    def move_west(self, val):
        self.x -= val

    def move_north(self, val):
        self.y -= val

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

def get_end_position(steps):
    point = Point(0, 0)

    cmd_map = {
        'N': point.move_north,
        'S': point.move_south,
        'E': point.move_east,
        'W': point.move_west,
        'L': point.turn_left,
        'R': point.turn_right,
        'F': (lambda: point.directions[point.current_dir])(), # FIXME reactivity necessary
    }

    for step in steps:
        f, val = step[0], int(step[1:])
        cmd_map[f](val)
        print(point, cmd_map[f])

    return point

def solve(x):
    return get_end_position(x)

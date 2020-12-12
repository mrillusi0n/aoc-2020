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
        self.y -= val

    def move_west(self, val):
        self.x -= val

    def move_north(self, val):
        self.y += val

    def translate(self, x, y):
        self.x += x
        self.y += y

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

class WayPoint(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.start = Point(0, 0)

    def turn_left(self, degrees):
        for _ in range(degrees // 90):
            self.x, self.y = -self.y, self.x
    
    def turn_right(self, degrees):
        for _ in range(degrees // 90):
            self.x, self.y = self.y, -self.x

    def move(self, val):
        self.start.translate(val * self.x, val * self.y)

def get_end_position(steps):
    point = WayPoint(10, 1)

    cmd_map = {
        'N': point.move_north,
        'S': point.move_south,
        'E': point.move_east,
        'W': point.move_west,
        'L': point.turn_left,
        'R': point.turn_right,
        'F': point.move,
    }

    for step in steps:
        f, val = step[0], int(step[1:])
        cmd_map[f](val)
        print(step, point, point.start)

    return point.start.manhattan_distance()

def solve(x):
    return get_end_position(x)

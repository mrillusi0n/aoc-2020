import re
from collections import defaultdict, Counter

def read_input(file):
    return list(map(str.rstrip, file.readlines()))

def shiny_bag_reachable(bag_color, relations):
    print(f'Checking if {bag_color} can have a shiny gold bag')
    bag = relations[bag_color]
    if 'shiny gold' in bag or bag['can_shine']:
        print(f'{bag_color} can hold a shiny gold bag!')
        return True

    child_bags = bag.keys() - {'can_shine'}
    print(f'Removed memo key: {child_bags}')

    for c_bag in child_bags:
        if shiny_bag_reachable(c_bag, relations):
            print(f'{bag_color} can hold a shiny gold bag!')
            relations[c_bag]['can_shine'] = True
            return True

    return False

def load_relations(lines):
    info = defaultdict(Counter)

    for s in lines:
        t = re.sub(r'[^\w ,]| ?\b(?:bags?|no|other|contain)\b', '', s)
        ctype, color, *rest = t.split(maxsplit=2)
        # info[f'{ctype} {color}']['can_shine'] = False

        for p in rest:
            for q in p.split(', '):
                count, color_name = q.split(maxsplit=1)
                info[f'{ctype} {color}'][color_name] = int(count)

    return info # 44, 38, 41, 55, 54, 39, 67

def count_inner_bags(bag_color, relations):
    inner_bags = relations[bag_color]
    print(f'{bag_color} contains {inner_bags}')

    if not inner_bags:
        return 1

    total = 0
    for bag in inner_bags:
        print(f'{inner_bags[bag]} * {bag}')
        total += (count := inner_bags[bag] * count_inner_bags(bag, relations))



    # return 1 + sum(inner_bags[bag] * count_inner_bags(bag, relations) for bag in inner_bags)
    return total + 1

def get_shiny_holders(relations):
    return sum(shiny_bag_reachable(bag, relations) for bag in relations)

def solve(data):
    return count_inner_bags('shiny gold', load_relations(data)) - 1

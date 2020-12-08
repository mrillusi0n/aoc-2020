import re
from collections import defaultdict, Counter

def read_input(file):
    return list(map(lambda x: x.rstrip(), file.readlines()))

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
        info[f'{ctype} {color}']['can_shine'] = False

        for p in rest:
            for q in p.split(', '):
                count, color_name = q.split(maxsplit=1)
                info[f'{ctype} {color}'][color_name] = int(count)

    return info # 44, 38, 41, 55, 54, 39, 67

def get_shiny_holders(relations):
    return sum(shiny_bag_reachable(bag, relations) for bag in relations)

def solve(data):
    return get_shiny_holders(load_relations(data))

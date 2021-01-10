from importlib import import_module
import argparse
import os

SOLVER_DEFAULT_CONTENT = '''\
def parse_input(text):
    pass

def solve(data):
    pass
'''

def create(args):
    dir_name = f'{args.n}_{args.t}'

    os.makedirs(dir_name, exist_ok=True) # 7_bags -> input.txt, __init__.py
    
    with open(os.path.join(dir_name, 'input.txt'), 'w'): pass
    with open(os.path.join(dir_name, '__init__.py'), 'w') as solver:
        solver.write(SOLVER_DEFAULT_CONTENT)

def get_input_text(problem_dir):
    with open(os.path.join(problem_dir, 'input.txt')) as f:
        return f.read()

def run_mod(mod, input_text):
    return mod.solve(mod.parse_input(input_text))

def run(args):
    dir_names = map(lambda d: d.name, # os.DirEntry.name,
                    filter(lambda d: d.name.split('_', maxsplit=1)[0].isdigit(),
                           os.scandir()))

    if day := args.day:
        dir_names = filter(
            lambda dir_name: dir_name.startswith(str(day)),
            dir_names)

    answers = {}

    for d in dir_names:
        day, problem_title = d.split('_', maxsplit=1)
        answers[day] = run_mod(import_module(d), get_input_text(d)) # f"Day {day} — {' '.join(problem_title.split('_')).title()}"

    print(answers)


parser = argparse.ArgumentParser(description='A simple tool to manage Advent of Code problems.')
subparsers = parser.add_subparsers(dest='cmd', required=True)

create_parser = subparsers.add_parser('create')
run_parser = subparsers.add_parser('run')

run_parser.add_argument('--day', '-d', metavar='D', type=int,
                    help='Run the Dth day, or all if not specified.')
run_parser.add_argument('--part', '-p', metavar='P', type=int,
                    help='Run the specified part, or both if not.')
run_parser.set_defaults(handler=run)

create_parser.add_argument('n', metavar='N', type=int,
                    help='Create the dir structure for day `n`')
create_parser.add_argument('t', metavar='T', type=str,
                    help='Title of the problem')
create_parser.set_defaults(handler=create)

args = parser.parse_args()

args.handler(args)
# --run 1

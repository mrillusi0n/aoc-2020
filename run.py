from shuttle_search import solve, read_input

def main():
    with open('shuttle_search/input.txt') as f:
        tests = read_input(f)
        print(solve(tests))

if __name__ == '__main__':
    main()

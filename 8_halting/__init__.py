def read_input(f):
    return list(map(lambda x: x.rstrip(), f.readlines()))

def execute(instructions):
    regs = [0, 0]
    executed = set()

    op_codes = {
        'acc': (1, lambda x: regs[1] + x),
        'nop': (0, lambda _: regs[0]),
        'jmp': (0, lambda x: regs[0] + x - 1),
    }

    for _ in instructions:
        print(regs, executed)
        i = instructions[regs[0]]

        if (regs[0], i) in executed:
            print(f'{i} already executed, breaking.')
            break

        print(f'Executing {i}')
        op, val = i.split()
        val = int(val)


        r, f = op_codes[op]

        executed.add((regs[0], i))

        regs[r] = f(val)
        regs[0] += 1


    return regs[1]

def solve(x):
    return execute(x)

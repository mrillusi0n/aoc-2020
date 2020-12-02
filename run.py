def get_inputs(folder):
    with open(folder + '/input.txt') as input_file:
        inputs = input_file.readlines()

    return inputs


from passwords import solve

print(solve(get_inputs('passwords')))

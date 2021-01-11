def read_input(f):
    return list(map(lambda x: int(x.rstrip()), f.readlines()))

def get_nums(nums, num):
    preamble = set(nums)
    for n in preamble:
        if abs(n - num) in preamble - {n}:
            return num

    return 0

def get_rule_breaker(nums, count):
    for i, num in enumerate(nums[count:]):
        if not get_nums(nums[i:i+count], num):
            return num

    return -1

def break_encryption(nums):
    breaker = get_rule_breaker(nums, 25)
    running_sum = 0
    block = []

    print(breaker)

    for num in nums:
        running_sum += num

        block.append(num)

        while running_sum > breaker:
            running_sum -= block.pop(0)

        if running_sum == breaker:
            break
        

    return min(block) + max(block), sum(block) == breaker

def solve(i):
    return break_encryption(i)

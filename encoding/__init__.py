def read_input(f):
    return list(map(lambda x: int(x.rstrip()), f.readlines()))

def get_nums(nums, num):
    preamble = set(nums)
    for n in preamble:
        if abs(n - num) in preamble - {n}:
            return num

    return 0

def get_rule_breaker(nums):
    for i, num in enumerate(nums[25:]):
        if not get_nums(nums[i:i+25], num):
            return num

    return -1

def break_encryption(nums):
    breaker = get_rule_breaker(nums)
    running_sum = 0
    block = []

    for num in nums:
        if running_sum == breaker:
            break
        if running_sum > breaker:
            running_sum -= block[0]
            del block[0]
        
        running_sum += num
        block.append(num)

    return block


def solve(i):
    return get_rule_breaker(i)

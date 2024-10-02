from functools import lru_cache 


target = 712
nums = [3, 1, 6]



def cansum(target, nums, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        if cansum(target-num, nums, memo) == 1:
            memo[target] = 1
            return True

    memo[target] = 0
    return False

print(cansum(target, nums))

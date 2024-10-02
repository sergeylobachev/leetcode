nums = [5, 4, 1]
target = 8

def howsum(target, nums, memo = {}):
    if target == 0: 
        return []
    if target < 0: 
        return None

    for num in nums:
        remainder = target - num
        if remainder in memo:
            return memo[remainder]
        else:
            remainderResult = howsum(remainder, nums)
            if remainderResult is not None:
                memo[remainder] = remainderResult + [num]
                return remainderResult + [num]

    return None

print(howsum(target, nums))
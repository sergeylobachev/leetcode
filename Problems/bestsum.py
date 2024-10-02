

def solution(target, nums, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in nums:
        remainder = target - num
        remainderResult = solution(remainder, nums, memo)
        if remainderResult != None:
            combination = remainderResult + [num]
            if shortest_combination == None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[remainder] = shortest_combination
    return shortest_combination

nums = [5, 3, 4, 7]
target = 13

print(solution(target, nums))
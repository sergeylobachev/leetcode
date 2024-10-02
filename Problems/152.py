from math import inf

def solution(nums):
    best = max(nums)

    mx = 1
    mn = 1

    for num in nums:
        mx, mn = max(num, mn*num, mx*num), min(num, mn*num, mx*num)
        print(mx, mn)
        best = max(best, mx)

    return best
    
nums = [2,3,-2,4]
nums = [-2, 3, 2, 0, 2, -1]
print(solution(nums))
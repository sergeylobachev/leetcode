from math import inf

def solution(nums):
    N = len(nums)

    dp = [nums[0], -inf]
    for i in range(1, N):
        dp[0], dp[1] = max(dp) + nums[i], dp[0] - nums[i]
        
    return max(dp)

nums = [1,-2,3,4]
# nums = [1,-1,1,-1]
# nums = [0]
# nums = [1,-1]
# nums = [-937]
print(solution(nums))
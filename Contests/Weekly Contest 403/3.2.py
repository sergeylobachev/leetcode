def solution(nums):
    N = len(nums)
    dp = [0] * (N+1)
    dp[1] = nums[0]

    for i in range(2, N+1):
        dp[i] = max(dp[i-1] + nums[i-1], dp[i-2] + nums[i-2] - nums[i-1])

    return dp[-1]

nums = [1,-2,3,4]

print(solution(nums))
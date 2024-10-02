def solution(nums):
    N = len(nums)
    dp = [0] * (N+2)
    dp[2] = nums[0]

    for i in range(1, N):
        if nums[i] >= 0:
            dp[i+2] = dp[i+1] + nums[i]
        elif nums[i] < 0:
            dp[i+2] = max(dp[i+1] + nums[i], dp[i] + nums[i-1] - nums[i])

    return dp[-1]



nums = [1,-2,3,4]
nums = [1,-1,1,-1]
nums = [0]
nums = [1,-1]
nums = [-937]
print(solution(nums))



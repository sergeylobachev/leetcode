def solution(nums, k):

    cost = [max(0, k-num) for num in nums]

    dp = [-1] * len(nums)
    dp[0] = cost[0]
    dp[1] = cost[1]
    dp[2] = cost[2]

    for i in range(3, len(nums)):
        dp[i] = cost[i] + min(dp[i-3:i])

    return min(dp[-3:])


nums = [2,3,0,0,2]
k = 4

nums = [0,1,3,3]
k = 5

print(solution(nums, k))
def solution(nums):
    N = len(nums)
    dp = [1] * N

    for i in range(1, N):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] += dp[j]

    return sum(dp)


nums = [1,3,5,4,7]

print(solution(nums))
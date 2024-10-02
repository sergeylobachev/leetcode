def solution(nums):
    dp = [1, 1]
    N = len(nums)

    ans = 1

    for i in range(1, N):
        if nums[i] == nums[i-1]:
            dp = [1, 1]
        elif nums[i] > nums[i-1]:
            dp = [dp[1] + 1, 1]
        else:
            dp = [1, dp[0] + 1]

        ans = max(ans, dp[0], dp[1])

    return ans


nums = [9,4,2,10,7,8,8,1,9]

print(solution(nums))
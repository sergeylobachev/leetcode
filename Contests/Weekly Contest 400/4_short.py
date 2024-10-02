def solution(nums, k):

    dp = [set() for num in nums]
    ans = 10 ** 9
    for idx, num in enumerate(nums):
        if idx == 0:
            dp[0].add(num)
        else:
            dp[idx].add(num)
            for prev in dp[idx-1]:
                dp[idx].add(prev & num)

        for candidate in dp[idx]:
            ans = min(ans, abs(candidate - k))

    return ans




nums = [1,2,4,5]
k = 3

nums = [1,2,1,2]
k = 2

nums = [1]
k = 10

print(solution(nums, k))
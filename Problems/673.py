def solution(nums):

    N = len(nums)

    # [maxlen, count]
    dp = [[1, 1] for _ in range(N)]

    for i, num in enumerate(nums):
        maxlen = 1
        count = 0
        for j in range(i):
            if nums[j] < num:
                if dp[j][0] == maxlen:
                    count += dp[j][1]

                if dp[j][0] > maxlen:
                    maxlen = dp[j][0]
                    count = dp[j][1]

        dp[i][0] = max(1, maxlen+1)
        dp[i][1] = max(1, count)

    maxlen = 1
    ans = 1
    for i in range(N):
        if dp[i][0] == maxlen:
            ans += dp[i][1]
        if dp[i][0] > maxlen:
            maxlen = dp[i][0]
            ans = dp[i][1]

    return ans



nums = [1,3,5,4,7]
# nums = [2,2,2,2,2]
print(solution(nums))
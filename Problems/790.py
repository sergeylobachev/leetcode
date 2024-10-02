def solution(n):
    if n == 1:
        return 1
    if n ==2:
        return 2
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, len(dp)):
        m = 0
        for j in range(1, i):
            m = max(m, dp[i-j] + dp[j])
        dp[i] = m + 2

    return dp[-1]

print(solution(3))
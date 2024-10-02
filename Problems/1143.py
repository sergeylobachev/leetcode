def solution(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    dp = [[0] * (l1+1) for _ in range(l2+1)]

    for i, a in enumerate(s1):
        for j, b in enumerate(s2):
            if a == b:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    return dp[-1][-1]



s1 = "abcde"
s2 = "ace" 

s1 = "abc"
s2 = "abc"

s1 = "abc"
s2 = "def"

print(solution(s1, s2))


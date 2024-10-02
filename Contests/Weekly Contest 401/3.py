def solution(rewardValues):

    r = rewardValues
    r.sort()
    N = len(r)
    ans = 0
    print(r)

    dp = [set() for _ in range(N)]
    dp[0].add(r[0])
    dp[0].add(0)

    for i in range(1, N):
        for val in dp[i-1]:
            dp[i].add(val)
            if val < r[i]:
                dp[i].add(val + r[i])

    print(dp)
    return max(dp[-1])

rewardValues = [1,6,4,3,2]
# rewardValues = [1,1,3,3]
# rewardValues = [1,4,5]
# rewardValues = [1,13,14,19]
print(solution(rewardValues))

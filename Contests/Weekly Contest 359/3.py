from collections import defaultdict


def solution(n, offers):

    dp = [0] * (n+1)
    d = defaultdict(list)

    for offer in offers:
        l, r, g = offer
        d[r].append([l, r, g])

    
    for i in range(1, n+1):
        
        offers = d[i-1]
        for offer in offers:
            print(i, offer)
            l, r, g = offer
            dp[i] = max(dp[i], g + dp[l])

        dp[i] = max(dp[i], dp[i-1])

    print(d)
    print(dp)

    return dp[-1]


n = 5
offers = [[0,0,1],[0,2,2],[1,3,2]]

# n = 5
# offers = [[0,0,1],[0,2,10],[1,3,2]]

print(solution(n, offers))
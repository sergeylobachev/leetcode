from math import inf

def solution(prices):
    N = len(prices)
    dp = [inf for _ in range(N)] + [0 for _ in range(5*N)]
    
    for i in range(N-1, -1, -1):
        dp[i] = prices[i]
        mn = 10 ** 5
        for j in range(i+1, 2*i + 3):
            mn = min(mn, dp[j])
        dp[i] += mn
        print(i, dp)
        
    return dp[0]

prices = [1,10,1,1]
prices = [26,18,6,12,49,7,45,45]

print(solution(prices))



def solution(days, costs):
    dp = [0 for _ in range(days[-1] + 1)]
    days = set(days)
    for i in range(len(dp)):
        if i in days:
            od = dp[max(0, i-1)] + costs[0]
            sd = dp[max(0, i-7)] + costs[1]
            td = dp[max(0, i-30)] + costs[2]
            dp[i] = min(od, sd, td)
        else:
            dp[i] = dp[i-1]
        print(dp)
    return dp[-1]

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

print(solution(days, costs))
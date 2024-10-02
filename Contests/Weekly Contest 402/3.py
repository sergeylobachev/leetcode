from collections import Counter
from collections import defaultdict

def solution(power):

    cost = defaultdict(int)
    for p in power:
        cost[p] += p

    cost[-2] = 0
    cost[-3] = 0
    spell = list(cost.keys())
    spell.sort()

    # print(spell)


    N = len(spell)
    dp = [0] * N

    for i in range(2, N):
        j = i-1
        while spell[j] >= spell[i] - 2:
            j -= 1
            
        dp[i] = max(dp[i-1], dp[i-2], cost[spell[i]] + dp[j])
    
    # print(dp)
    return max(dp)


# power = [1,1,3,4]
# power = [7,1,6,6]
power = [5,9,2,10,2,7,10,9,3,8]
print(solution(power))
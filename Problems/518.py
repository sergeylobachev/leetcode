# from collections import defaultdict

# def solution(amount, coins):
#     N = len(coins)
#     dp = [[0 for _ in range(amount+1)] for _ in range(N)]

    
#     for i in range(N):
#         dp[i][0] = 1

#     for j in range(1, amount+1):
#         if j % coins[0] == 0:
#             dp[0][j] = 1

#     for i in range(1, N):
#         for j in range(1, amount + 1):
#             dp[i][j] += dp[i-1][j]
#             if j - coins[i] >= 0:
#                 dp[i][j] += dp[i][j-coins[i]]

#     return dp[-1][-1]



# amount = 5
# coins = [1,2,5]

# print(solution(amount, coins))

a = 0
if a:
    print("yes")

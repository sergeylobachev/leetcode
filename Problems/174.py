dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

def solution(dungeon):
    rows = len(dungeon)
    cols = len(dungeon[0])

    dp = [[0]*(cols+1) for i in range(rows+1)]

    for i in range(rows+1):
        dp[i][-1] = float("inf")

    for j in range(cols+1):
        dp[-1][j] = float("inf")

    dp[-1][-2] = 1

    for i in range(rows-1, -1 , -1):
        for j in range(cols-1, -1, -1):
            dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

    return dp[0][0]

solution(dungeon)
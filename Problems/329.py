def solution(matrix):
    R, C = len(matrix), len(matrix[0])
    dp = [[-1 for _ in range(C)] for _ in range(R)]

    def dfs(x, y):
        if dp[x][y] > -1:
            return dp[x][y]

        neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        ml = 1
        for xn, yn in neighbours:
            if 0 <= xn < R and 0 <= yn < C and matrix[x][y] > matrix[xn][yn]:
                ml = max(ml, 1 + dfs(xn, yn))

        dp[x][y] = ml
        return ml

    
    for i in range(R):
        for j in range(C):
            dp[i][j] = dfs(i, j)


    answer = max([max(row) for row in dp])

    return answer

 
matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[3,4,5],[3,2,6],[2,2,1]]
matrix = [[1]]
matrix = [[7,8,9],[9,7,6],[7,2,3]]
print(solution(matrix))


    
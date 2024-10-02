def solution(grid):
    R = len(grid)
    C = len(grid[0])
    helper = [[[0, 0, 0, 0] for i in range(C)] for j in range(R)]

    for i in range(R):
        s = 0
        for j in range(C):
            if grid[i][j] == 1:
                s += 1
            helper[i][j][0] = s

    for i in range(R):
        s = 0
        for j in range(C-1, -1, -1):
            if grid[i][j] == 1:
                s += 1
            helper[i][j][1] = s

    for i in range(C):
        s = 0
        for j in range(R):
            if grid[j][i] == 1:
                s += 1
            helper[j][i][2] = s


    for i in range(C):
        s = 0
        for j in range(R-1, -1 , -1):
            if grid[j][i] == 1:
                s += 1
            helper[j][i][3] = s


    ret = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                ret += (helper[i][j][0] -1)  * (helper[i][j][2] - 1)
                ret += (helper[i][j][0] -1)  * (helper[i][j][3] - 1)
                ret += (helper[i][j][1] -1)  * (helper[i][j][2] - 1)
                ret += (helper[i][j][1] -1)  * (helper[i][j][3] - 1)


    return ret

# grid = [[0,1,0],[0,1,1],[0,1,0]]
# grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
grid = [[1,0,1],[1,0,0],[1,0,0]]
print(solution(grid))
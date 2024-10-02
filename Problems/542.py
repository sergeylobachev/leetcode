from math import inf

def solution(mat):
    R = len(mat)
    C = len(mat[0])

    ans = [[inf] * C for _ in range(R)]

    q = []

    for i in range(R):
        for j in range(C):
            if mat[i][j] == 0:
                mat[i][j] = -1
                ans[i][j] = 0
                q.append([i, j])

    while q:
        x, y  = q.pop(0)
        offsets = [[-1,0], [0,1], [1,0], [0,-1]]
        for o in offsets:
            newx = x + o[0]
            newy = y + o[1]
            if 0 <= newx <= R-1 and 0 <= newy <= C-1 and mat[newx][newy] != -1:
                ans[newx][newy] = ans[x][y] + 1
                mat[newx][newy] = -1
                q.append([newx, newy])

    return ans

mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
print(solution(mat))

    



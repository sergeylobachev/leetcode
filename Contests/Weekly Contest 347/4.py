from collections import defaultdict


def solution(mat):
    R = len(mat)
    C = len(mat[0])

    ## unique values
    uvals = defaultdict(list)
    for i in range(R):
        for j in range(C):
            uvals[mat[i][j]].append((i, j))

    dp = [[0 for _ in range(C)] for _ in range(R)]
    rmax = [0] * R
    cmax = [0] * C

    for val in sorted(uvals.keys(), reverse = True):
        for x, y in uvals[val]:
            dp[x][y] = 1 + max(rmax[x], cmax[y])
        for x, y in uvals[val]:
            rmax[x] = max(rmax[x], dp[x][y])
            cmax[y] = max(cmax[y], dp[x][y])


    return max(max(rmax), max(cmax))


mat = [[3,1],[3,4]]
mat = [[1,1],[1,1]]
mat = [[3,1,6],[-9,5,7]]
print(solution(mat))

    


    
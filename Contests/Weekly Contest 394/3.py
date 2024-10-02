import string
from collections import Counter

def solution(grid):
    R = len(grid)
    C = len(grid[0])

    m = [[R] * C for i in range(10)]

    for i in range(R):
        for j in range(C):
            m[grid[i][j]][j] -= 1

    
    for j in range(1, C):
        for i in range(10):
            mv = float("inf")
            for k in range(10):
                if m[k][j-1] < mv and k != i:
                    mv = m[k][j-1]
            m[i][j] += mv

    a = float("inf")
    for i in range(10):
        if m[i][-1] < a:
            a = m[i][-1]

    
    return a


l = string.ascii_lowercase
print(l)

# grid = [[1,1,1],[0,0,0]]
# grid = [[1,0,2],[1,0,2]]
grid = [[1],[2],[3]]
print(solution(grid))


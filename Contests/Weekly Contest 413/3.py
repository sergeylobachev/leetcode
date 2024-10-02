from collections import defaultdict
from functools import cache

def solution(grid):
    R = len(grid)
    C = len(grid[0])

    d = defaultdict(list)
    for i in range(R):
        for j in range(C):
            d[grid[i][j]].append(i)

    print(d)

    def go(num, bitmask):
        
        if num == 101:
            return 0

        ans = 0
        if num in d:
            for row in d[num]:
                print(num, row)
                if not bitmask & (1 << row):
                    ans = max(ans, num + go(num+1, bitmask | (1 << row)))
        ans = max(ans, go(num+1, bitmask))

        return ans


    return go(1, 0)


grid = [[8,7,6],[8,3,2]]
grid = [[1,2,3],[4,3,2],[1,1,1]]


print(solution(grid))


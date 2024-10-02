from functools import lru_cache

@lru_cache(maxsize=None)
def solution(grid):
    R = len(grid)
    C = len(grid[0])

    mx = [max(row) for row in grid]
    print(mx)

    @cache
    def go(row, selected):
        if row == R:
            return sum(selected)
        
        ans = 0
        for j in range(C):
            if grid[row][j] not in selected:
                ans = max(ans, go(row+1, selected + (grid[row][j],)))
        ans = max(ans, go(row+1, selected))

        return ans

    return go(0, ())


grid = [[1,2,3],[4,3,2],[1,1,1]]
grid = [[8,7,6],[8,3,2]]

print(solution(grid))
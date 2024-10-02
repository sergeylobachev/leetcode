from itertools import permutations

def solution(grid):
    gaps = []
    stones = []

    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                gaps.append((i,j))
            while grid[i][j] > 1:
                stones.append((i,j))
                grid[i][j] -= 1

    candidates = list(permutations(stones))
    answer = 1000

    for candidate in candidates:
        cur = 0
        for idx, stone in enumerate(candidate):
            x, y = stone
            cur += abs(gaps[idx][0] - x) + abs(gaps[idx][1] - y)
        answer = min(answer, cur)

    return answer

grid = [[1,1,0],[1,1,1],[1,2,1]]
grid = [[1,3,0],[1,0,0],[1,0,3]]
grid = [[3,2,0],[0,1,0],[0,3,0]]
grid = [[0,2,3],[2,0,1],[0,1,0]]
grid = [[4,0,0],[0,0,2],[3,0,0]]
print(solution(grid))
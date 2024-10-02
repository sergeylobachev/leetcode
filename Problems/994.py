from collections import deque

def solution(grid):
    R = len(grid)
    C = len(grid[0])

    fresh = set()
    rotten = deque([])

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                fresh.add((i, j))
            if grid[i][j] == 2:
                rotten.append([0,i,j])

    if len(fresh) == 0:
        return 0

    time = 0
    while time < 11:
        time += 1
        while rotten and rotten[0][0] == time-1:
            t, i, j = rotten.popleft()
            if (i-1,j) in fresh:
                fresh.discard((i-1, j))
                rotten.append([time, i-1, j])
            if (i+1,j) in fresh:
                fresh.discard((i+1, j))
                rotten.append([time, i+1, j])
            if (i,j-1) in fresh:
                fresh.discard((i, j-1))
                rotten.append([time, i, j-1])
            if (i,j+1) in fresh:
                fresh.discard((i, j+1))
                rotten.append([time, i, j+1])

        if len(fresh) == 0:
            return time

    return -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(solution(grid))
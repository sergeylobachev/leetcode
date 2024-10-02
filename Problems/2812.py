from collections import deque
from heapq import heappop, heappush

def solution(grid):
    N = len(grid)
    cost = [[-1 for _ in range(N)] for _ in range(N)]
    deq = deque()
    neighbours = [[0,-1], [0,1], [-1,0], [1,0]]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                deq.append((i,j))
                cost[i][j] = 0

    while deq:
        x, y = deq.popleft()
        for n in neighbours:
            nx = x + n[0]
            ny = y + n[1]
            if  0 <= nx < N and 0 <= ny < N and cost[nx][ny] == -1:
                deq.append((nx, ny))
                cost[nx][ny] = cost[x][y] + 1

    ## (cost, x, y)
    q = [(-cost[0][0], 0, 0)]
    processed = set()
    processed.add((0, 0))

    ans = [[0 for _ in range(N)] for _ in range(N)]
    ans[0][0] = cost[0][0]

    while q:
        c, x, y = heappop(q)
        processed.add((x,y))
        for n in neighbours:
            nx = x + n[0]
            ny = y + n[1]
            if (nx, ny) not in processed and 0 <= nx < N and 0 <= ny < N:
                ans[nx][ny] = min(-c, cost[nx][ny])
                heappush(q, (-ans[nx][ny], nx, ny))
                processed.add((nx, ny))

    return ans[-1][-1]

# grid = [[1,0,0],[0,0,0],[0,0,1]]
# grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
grid = [[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[1,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,1,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]]
print(solution(grid))





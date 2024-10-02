def solution(grid):
    R = len(grid)
    C = len(grid[0])

    ans = 0

    for x in range(R//2):
        for y in range(C//2):
            a = grid[x][y]
            b = grid[x][~y]
            c = grid[~x][y]
            d = grid[~x][~y]
            s = a + b + c + d
            if s == 1 or s == 3:
                ans += 1
            if s == 2:
                ans += 2

    ones = 0
    p = 0
    if R % 2:
        for i in range(C//2):
            if grid[R//2][i] == 0 and grid[R//2][~i] == 1:
                p += 1
                ans += 1

            if grid[R//2][i] == 1 and grid[R//2][~i] == 0:
                p += 1
                ans += 1

            if grid[R//2][i] == 1 and grid[R//2][~i] == 1:
                ones += 2

    if C % 2:
        for i in range(R//2):
            if grid[i][C//2] == 0 and grid[~i][C//2] == 1:
                p += 1
                ans += 1
            
            if grid[i][C//2] == 1 and grid[~i][C//2] == 0:
                p += 1
                ans += 1

            if grid[i][C//2] == 1 and grid[~i][C//2] == 1:
                ones += 2

    if R % 2 == 1 and C % 2 == 1:
        # ones += grid[R//2][C//2]
        ans += 1

    ones = ones % 4

    if ones == 2 and p == 0:
        ans += 2

    return ans


grid = [[1,0,0],[0,1,0],[0,0,1]]
grid = [[0,1],[0,1],[0,0]]
grid = [[1],[1]]
grid = [[1],[1],[1],[0]]

print(solution(grid))


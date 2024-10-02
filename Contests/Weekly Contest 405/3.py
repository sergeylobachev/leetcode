def solution(grid):

    R = len(grid)
    C = len(grid[0])

    ## stores X-Y, X if any
    ans = 0

    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                if grid[i][j] == "X":
                    grid[i][j] = [1, 1]
                elif grid[i][j] == "Y":
                    grid[i][j] = [-1, 0]
                else:
                    grid[i][j] = [0, 0]

                if grid[i][j][0] == 0 and grid[i][j][1] == 1:
                    ans += 1

            elif i == 0:
                if grid[i][j] == "X":
                    grid[i][j] = [grid[i][j-1][0] + 1, 1]

                elif grid[i][j] == "Y":
                    grid[i][j] = [grid[i][j-1][0] - 1, grid[i][j-1][1]]

                else:
                    grid[i][j] = [grid[i][j-1][0], grid[i][j-1][1]]

                if grid[i][j][0] == 0 and grid[i][j][1] == 1:
                    ans += 1

            elif j == 0:
                if grid[i][j] == "X":
                    grid[i][j] = [grid[i-1][j][0] + 1, 1]

                elif grid[i][j] == "Y":
                    grid[i][j] = [grid[i-1][j][0] - 1, grid[i-1][j][1]]

                else:
                    grid[i][j] = [grid[i-1][j][0], grid[i-1][j][1]]

                if grid[i][j][0] == 0 and grid[i][j][1] == 1:
                    ans += 1

            else:
                if grid[i][j] == "X":
                    c = grid[i-1][j][0] + grid[i][j-1][0] - grid[i-1][j-1][0] + 1
                    grid[i][j] = [c, 1]
                    
                elif grid[i][j] == "Y":
                    c = grid[i-1][j][0] + grid[i][j-1][0] - grid[i-1][j-1][0] - 1
                    isx = grid[i-1][j][1] | grid[i][j-1][1]
                    grid[i][j] = [c, isx]

                else:
                    c = grid[i-1][j][0] + grid[i][j-1][0] - grid[i-1][j-1][0]
                    isx = grid[i-1][j][1] | grid[i][j-1][1]
                    grid[i][j] = [c, isx]

                if grid[i][j][0] == 0 and grid[i][j][1] == 1:
                    ans += 1


    print(grid)
    return ans





grid = [["X","Y","."],["Y",".","."]]
grid = [["X","X"],["X","Y"]]
grid = [[".","."],[".","."]]

print(solution(grid))


def solution(grid):

    R = len(grid)
    C = len(grid[0])
    ans = float("-inf")

    for j in range(C-1, -1, -1):
        for i in range(R-1, -1, -1):
            if i == R-1:
                below = float("-inf")
            else:
                below = grid[i+1][j]
            
            if j == C-1:
                right = float("-inf")
            else:
                right = grid[i][j+1]

            ans = max(ans, max(below, right) - grid[i][j])
            grid[i][j] = max(grid[i][j], below, right)

    print(grid)
    return ans


# grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
grid = [[4,3,2],[3,2,1]]

print(solution(grid))

    




def solution(grid):
    for i in range(2):
        for j in range(2):
            b = 0
            w = 0
            for k in range(2):
                for l in range(2):
                    if grid[i+k][j+l] == "B":
                        b += 1
                    else:
                        w += 1
            if b > 2 or w > 2:
                return True

    return False

# grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
# grid = [["B","W","B"],["W","B","W"],["B","W","B"]]
grid = [["B","W","B"],["B","W","W"],["B","W","W"]]
print(solution(grid))
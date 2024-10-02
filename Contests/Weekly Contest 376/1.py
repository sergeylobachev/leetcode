from collections import defaultdict

def solution(grid):
    answer = [0, 0]
    d = defaultdict(int)
    
    n = len(grid)
    for i in range(n):
        for j in range(n):
            d[grid[i][j]] += 1

    print(d, n)
        
    for i in range(1, n*n + 1):
        if d[i] == 2:
            answer[0] = i
        if d[i] == 0:
            answer[1] = i
            
    return answer

grid = [[9,1,7],[8,9,2],[3,4,6]]

print(solution(grid))


def solution(board, word):
    N = len(word)
    R = len(board)
    C = len(board[0])

    def dfs(x, y, idx, visited):
        if idx == N:
            return True

        if not (0 <= x < R and 0 <= y < C) or (x, y) in visited or board[x][y] != word[idx]:
            return False 

        visited.add((x,y))
        l = dfs(x, y-1, idx+1, visited)
        r = dfs(x, y+1, idx+1, visited)
        u = dfs(x-1, y, idx+1, visited)
        d = dfs(x+1, y, idx+1, visited)

        visited.remove((x,y))
        
        return l or r or u or d

    for i in range(R):
        for j in range(C):
            if dfs(i, j, 0, visited):
                return True

    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

print(solution(board, word))




    



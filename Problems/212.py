class Trie:
    def __init__(self, *words):
        self.d = {}
        for word in words:
            self.add(word)

    def add(self, word):
        d = self.d
        for letter in word:
            d = d.setdefault(letter, {})
        d["__end__"] = True


    
def solution(board, words):
    R = len(board)
    C = len(board[0])


    T = Trie(*words)

    answer = set()
    visited = set()

    def dfs(x, y, d, prefix):
        if not(0 <= x < R and 0 <= y < C) or (x, y) in visited or board[x][y] not in d:
            return 

        visited.add((x,y))
        d = d[board[x][y]]
        prefix += board[x][y]
        if d.get("__end__"):
            answer.add(prefix)

        dfs(x+1, y, d, prefix)
        dfs(x-1, y, d, prefix)
        dfs(x, y+1, d, prefix)
        dfs(x, y-1, d, prefix)

        visited.remove((x,y))

    for i in range(R):
        for j in range(C):
            dfs(i, j, T.d, "")


    return list(answer)
    

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]



print(solution(board, words))
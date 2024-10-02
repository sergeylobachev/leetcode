from collections import Counter

def solution(board, word):
    R = len(board)
    C = len(board[0])
    answer = 0

    def search(i, j, word, visited):
        if len(word) == 0:
            return True

        if not (0 <= i < R and 0 <= j < C) or board[i][j] != word[0] or (i,j) in visited:
            return False

        visited.add((i, j))
        newWord = word[1:]


        l = search(i, j-1, newWord, visited)
        r = search(i, j+1, newWord, visited)
        u = search(i-1, j, newWord, visited)
        d = search(i+1, j, newWord, visited)

        visited.remove((i, j))

        return l or r or u or d

    for i in range(R):
        for j in range(C):
            visited = set()
            answer = answer or search(i, j, word, visited)

    return answer


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

print(solution(board, word))
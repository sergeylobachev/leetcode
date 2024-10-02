from math import inf

def solution(board):
    R = len(board)
    C = len(board[0])

    candidates = set()
    ans = -inf

    for i in range(R):
        row = [(board[i][j], j) for j in range(C)]
        row.sort(reverse = True)
        for k in range(3):
            candidates.add((i, row[k][1]))

    candidates = list(candidates)
    N = len(candidates)

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                a = candidates[i]
                b = candidates[j]
                c = candidates[k]
                if a[0] != b[0] and b[0] != c[0] and c[0] != a[0] and a[1] != b[1] and b[1] != c[1] and c[1] != a[1]:
                    ans = max(ans, board[a[0]][a[1]] + board[b[0]][b[1]] + board[c[0]][c[1]])

    return ans

board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]
board = [[1,2,3],[4,5,6],[7,8,9]]
board = [[1,1,1],[1,1,1],[1,1,1]]

print(solution(board))
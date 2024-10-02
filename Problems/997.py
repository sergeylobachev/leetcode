
def solution(n, trust):

    # filling adjacency matrix
    am = [[0] * n for i in range(n)]
    for a, b in trust:
        am[a-1][b-1] = 1

    i = 0 
    j = 0
    while j < n and j < n:
        if am[i][j] == 0 :
            i += 1
        else:
            j += 1

    if i < n and sum(am[i]) == 0 and sum([am[_][i] for _ in range(n)]) == n-1:
        return i+1

    else: 
        return -1
    


n = 3
trust = [[1,3],[2,3]]
print(solution(n, trust))
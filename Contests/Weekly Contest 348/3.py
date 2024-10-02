from collections import defaultdict

def solution(n, queries):

    ## type0 - row
    ## type1 - column

    N = len(queries)

    nq = []
    seen = set()
    for i in range(N-1, -1, -1):
        tp, idx, val = queries[i]
        if (tp, idx) not in seen:
            nq.append([tp, idx, val])
        seen.add((tp, idx))

    nq = nq[::-1]
    # print(nq)
    colsum = 0
    rowsum = 0
    sm = 0

    for tp, idx, val in nq:
        if tp == 0:
            sm += val * n - colsum
            rowsum += val

        if tp == 1:
            sm += val * n - rowsum
            colsum += val

    return sm



n = 3
queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]

n = 3
queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]

print(solution(n, queries))
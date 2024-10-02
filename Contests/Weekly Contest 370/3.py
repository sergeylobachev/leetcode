def solution(edges, values):
    N = len(values)
    S = sum(values)

    al = [set() for _ in range(N)]

    for edge in edges:
        a, b = edge
        al[a].add(b)
        al[b].add(a)

    def oriented(al, s):
        for child in al[s]:
            al[child].discard(s)
            oriented(al, child)

    oriented(al, 0)


    def dfs(s):
        if len(al[s]) == 0:
            return values[s]
        else:
            cursum = 0
            for child in al[s]:
                cursum += dfs(child)

            return min(values[s], cursum)

    return S - dfs(0)


edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [20,10,9,7,4,3,5]

print(solution(edges, values))
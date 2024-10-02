def dfs(al, s):
    time = 0

    def visit(al, u):
        nonlocal time
        time += 1
        d[u] = time
        color[u] = "gray"
        for v in al[u]:
            if color[v] == "white":
                parent[v] = u
                visit(al, v)
        time += 1
        f[u] = time
        color[u] = "black"

    N = len(al)
    color = ["white"] * N
    parent = [None] * N
    d = [0] * N ## d -- discovered timestamp
    f = [0] * N ## f -- finished timestamp
    
    for u in range(N):
        if color[u] == "white":
            visit(al, u)

    return d

al = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]
al = [[1,3],[4],[4,5],[1],[3],[5]]
print(dfs(al, 0))
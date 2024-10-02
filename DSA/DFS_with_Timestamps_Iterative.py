def dfs(al):
    time = 0

    N = len(al)
    color = ["white"] * N
    parent = [None] * N
    d = [0] * N ## d -- discovered timestamp
    f = [0] * N ## f -- finished timestamp

    s = []

    for u in range(N):
        if color[u] == "white":
            s.append((u, "start"))

            while s:
                node, action = s.pop()
                
                if action == "start":
                    if color[node] == "white":
                        time += 1
                        d[node] = time
                        color[node] = "gray"
                        s.append((node, "end"))
                        for v in reversed(al[node]):
                            if color[v] == "white":
                                parent[v] = node
                                s.append((v, "start"))
                elif action == "end":
                    time += 1
                    f[node] = time
                    color[node] = "black"

    return d

al = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]
al = [[1,3],[4],[4,5],[1],[3],[5]]
print(dfs(al))
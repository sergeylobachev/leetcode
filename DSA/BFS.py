def bfs(al, s):
    """
    al -- ajacency list
    s -- start vertex
    colors:
        white -- undiscovered vertices
        gray -- vertices on frontier
        black -- vertices behind frontier
    """
    V = len(al)
    color = ["white"] * V
    distance = [float("inf")] * V
    parent = [None] * V

    color[s] = "gray"
    distance[s] = 0

    q = []
    q.append(s)
    while q:
        u = q.pop(0)
        for v in al[u]:
            if color[v] == "white":
                color[v] = "gray"
                distance[v] = distance[u] + 1
                parent[v] = u
                q.append(v)
            color[u] = "black"

    return distance, parent

def shortestPath(al, s, e):
    distance, parent = bfs(al, s)
    if e == s:
        print(s)
    elif parent[e] == None:
        print(f"no path from {s} to {e} exists")
    else:
        shortestPath(al, s, parent[e])
        print(e)


al = [[1,2],[0,3,4],[0,5,6],[1],[1],[2],[2]]

# print(bfs(al, 6))
shortestPath(al, 6, 3)

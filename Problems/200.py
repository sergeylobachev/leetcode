def solution(grid):

    def bfs(al):
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
        components = 0

        for idx, s in enumerate(al):
            if color[idx] == "white" and len(al[idx]) > 0:
                color[idx] = "gray"
                distance[idx] = 0
                components += 1
                q = []
                q.append(idx)
                while q:
                    u = q.pop(0)
                    for v in al[u]:
                        if color[v] == "white":
                            color[v] = "gray"
                            distance[v] = distance[u] + 1
                            parent[v] = u
                            q.append(v)
                        color[u] = "black"

        return components

    R = len(grid)
    C = len(grid[0])

    al = [[] for _ in range(R*C)]

    counter = 0
    for i in range(R):
        for j in range(C):
            al[counter].append(i*C + j)
            if grid[i][j] == "1":
                al[counter].append(i*C + j)
                if i > 0: al[counter].append((i-1) * C + j)
                if i < R-1: al[counter].append((i+1) * C + j)
                if j > 0: al[counter].append(i * C + j-1)
                if j < C-1: al[counter].append(i * C + j+1)

            counter +=1
    print(al)
    return bfs(al)


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

grid = [["1"]]

print(solution(grid))
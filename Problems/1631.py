from heapq import heappop, heappush

def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist = [float("inf")] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if max(edge_len, path_len) < dist[w]:
                    dist[w] = max(edge_len, path_len)
                    heappush(queue, (max(edge_len, path_len), w))

    return dist

def solution(heights):
    R = len(heights)
    C = len(heights[0])

    def converter(r, c):
        return r * C + c

    al = [[] for _ in range(R*C)]


    for i in range(R):
        for j in range(C):
            if i > 0:
                al[converter(i, j)].append((converter(i-1, j), abs(heights[i][j] - heights[i-1][j])))

            if j > 0:
                al[converter(i, j)].append((converter(i, j-1), abs(heights[i][j] - heights[i][j-1])))

            if i < R-1:
                al[converter(i, j)].append((converter(i+1, j), abs(heights[i][j] - heights[i+1][j])))

            if j < C-1:
                al[converter(i, j)].append((converter(i, j+1), abs(heights[i][j] - heights[i][j+1])))

    distance = dijkstra(al, 0)
    return distance[-1]



heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(solution(heights))

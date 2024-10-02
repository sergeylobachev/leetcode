from collections import defaultdict
from heapq import heappush
from heapq import heappop

def solution(n, edges, prob, start, end):

    graph = defaultdict(list)

    ## building an adjacency map
    for i, edge in enumerate(edges):
        a, b = edge
        graph[a].append((b, prob[i]))
        graph[b].append((a, prob[i]))

    distances = [0] * n
    distances[start] = 1

    ## in our heap we'll store (-path_len, vertex)
    h = [(-1, start)]
    while h:
        path_len, u = heappop(h)
        if -path_len == distances[u]:
            for v, edge_len in graph[u]:
                if edge_len * -path_len > distances[v]:
                    distances[v] = edge_len * -path_len
                    heappush(h, (edge_len * path_len, v))
        print(distances)

    return distances[end]



n = 3
edges = [[0,1],[1,2],[0,2]]
prob = [0.5,0.5,0.2]
start = 0
end = 2


n = 3
edges = [[0,1],[1,2],[0,2]]
prob = [0.5,0.5,0.3]
start = 0
end = 2

n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2


print(solution(n, edges, prob, start, end))


## logarithmic probability
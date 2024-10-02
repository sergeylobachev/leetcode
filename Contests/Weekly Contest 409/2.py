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
                if edge_len + path_len < dist[w]:
                    dist[w] = edge_len + path_len
                    heappush(queue, (edge_len + path_len, w))

    return dist

def solution(n, queries):
    graph = [[] for _ in range(n)]

    for i in range(n-1):
        graph[i].append((i+1, 1))

    ans = []

    for u, v in queries:
        graph[u].append((v, 1))
        dist = dijkstra(graph, 0)
        ans.append(dist[-1])

    return ans



    
n = 5
queries = [[2,4],[0,2],[0,4]]

n = 4
queries = [[0,3],[0,2]]
print(solution(n, queries))

from heapq import heappop, heappush
from collections import defaultdict
from math import inf

def dijkstra(graph, start):
    """ 
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist

def solution(source, target, original, changed, cost):
    N = len(cost)
    d = defaultdict(int)
    graph = [[] for _ in range(26)]

    for i in range(N):
        if (original[i], changed[i]) in d:
            d[(original[i], changed[i])] = min(d[(original[i], changed[i])], cost[i])
        else:
            d[(original[i], changed[i])] = cost[i]

    for edge in d:
        iv, ov = edge
        cost = d[edge]
        iv = ord(iv) - ord("a")
        ov = ord(ov) - ord("a")
        graph[iv].append((ov, cost))

    am = [[inf for _ in range(26)] for _ in range(26)]

    for start in range(26):
        am[start] = dijkstra(graph, start)
        
    ans = 0
    for i in range(len(source)):
        iv = ord(source[i]) - ord("a") 
        ov = ord(target[i]) - ord("a")
        if am[iv][ov] == inf:
            return -1
        else:
            ans += am[iv][ov]       

    return ans


source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]

source = "aaaa"
target = "bbbb"
original = ["a","c"]
changed = ["c","b"]
cost = [1,2]

print(solution(source, target, original, changed, cost))
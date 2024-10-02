from collections import defaultdict
from functools import cache


def solution(edges):

    deg = defaultdict(int)
    N = len(edges)
    for edge in edges:
        deg[edge] += 1

    q = list([u for u in range(N) if deg[u] == 0])
    while q:
        u = q.pop(0)
        v = edges[u]
        deg[v] -= 1
        if deg[v] == 0:
            q.append(v)

    
    count = defaultdict(int)
    vis = set()

    for u in [i for i in range(N) if deg[i] != 0]:
        if u in vis:
            continue
        cycle = []
        while u not in vis:
            cycle.append(u)
            vis.add(u)
            u = edges[u]
        
        for v in cycle:
            count[v] = len(cycle)

    @cache
    def dfs(v):
        if v in count: 
            return count[v]
        else:
            return 1 + dfs(edges[v])

    return [dfs(v) for v in range(N)]



    
    


edges = [1,2,0,0]
edges = [1,2,3,4,0]

edges = [1,2,0,0]
edges = [1,2,3,4,0]
edges = [6,3,6,1,0,8,0,6,6]

print(solution(edges))
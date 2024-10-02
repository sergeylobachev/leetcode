from collections import defaultdict
from collections import deque

def solution(edges):
    d = defaultdict(list)
    for a, b in edges:
        d[a].append(b)
        d[b].append(a)

    N = len(edges) + 1
    size = [0] * N
    visited = set()

    def dfs(u):
        visited.add(u)
        ret = 1
        for v in d[u]:
            if v not in visited:
                ret += dfs(v)
        size[u] = ret
        return ret

    dfs(0)

    ans = 0
    visited = set()
    q = deque()
    q.append(0)

    while q:
        u = q.popleft()
        visited.add(u)
        children = set()
        for v in d[u]:
            if v not in visited:
                q.append(v)
                children.add(size[v])

        if len(children) < 2:
            ans += 1


    return ans




edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
# edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]

print(solution(edges))






        



    
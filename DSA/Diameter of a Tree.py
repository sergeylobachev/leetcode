from collections import defaultdict



def diameter(al):
    """
    We assume that we have adjacency list for n nodes numbered from 0 to n-1.
    Starting from node s (starting node) we find the farthest node x. After that we run BFS 
    one more time and determining node y (farthest mode from x). x <--> y will be the diameter of our tree.
    """
    s = 0
    q = [(s, 0)]
    visited = set()
    max_distance = 0
    furthest = s
    while q:
        u, distance = q.pop()
        if distance > max_distance:
            max_distance= distance
            furthest = u
        visited.add(u)
        for v in al[u]:
            if v not in visited:
                q.append((v, distance+1))

    x = furthest
    q = [(x, 0)]
    visited = set()
    max_distance = 0
    furthest = x
    while q:
        u, distance = q.pop()
        if distance > max_distance:
            max_distance= distance
            furthest = u
        visited.add(u)
        for v in al[u]:
            if v not in visited:
                q.append((v, distance+1))

    diameter = max_distance
    return diameter


edges = [[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]]
edges = [[0,1]]
edges = [[0,1],[0,2],[0,3]]

al = [[] for _ in range(len(edges) + 1)]
for u, v in edges:
    al[u].append(v)
    al[v].append(u)


print(diameter(al))




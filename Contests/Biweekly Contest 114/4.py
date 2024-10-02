from collections import defaultdict

def solution(n, edges, values, k):
    components = 0
    al = defaultdict(list)
    for u, v in edges:
        al[u].append(v)
        al[v].append(u)

    leafs = []

    for u in al.keys():
        if len(al[u]) == 1:
            leafs.append(u)

    while len(leafs) > 0:
        u = leafs.pop(0)
        if not al[u]:
            continue
        v = al[u][0]
        if values[u] % k == 0:
            components += 1
            al[v].remove(u)
            if len(al[v]) == 1:
                leafs.append(v)
        else:
            al[v].remove(u)
            if len(al[v]) == 1:
                leafs.append(v)
            values[v] += values[u]

    return components+1


n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6

n = 7
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [3,0,6,1,5,2,1]
k = 3

print(solution(n, edges, values, k))


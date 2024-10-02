def solution(N, edges):

    if N == 1:
        return [0]

    al = [[] for _ in range(N)]

    for e in edges:
        a, b = e
        al[a].append(b)
        al[b].append(a)

    leafs = []
    for idx, av in enumerate(al):
        if len(av) == 1:
            leafs.append(idx)

    print(leafs)

    while N > 2:
        newleafs = []
        for leaf in leafs:
            v = al[leaf].pop()
            al[v].remove(leaf)
            if len(al[v]) == 1:
                newleafs.append(v)
            N -= 1
        leafs = newleafs

    return leafs

n = 4
edges = [[1,0],[1,2],[1,3]]

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

# n = 3
# edges = [[0,1],[0,2]]

# n = 7
# edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]

print(solution(n, edges))

    

    

    
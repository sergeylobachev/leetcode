

def solution(m, n, hFences, vFences):
    MOD = 10 ** 9 + 7
    hset = set()
    hset.add(m - 1)



    for i, hFence in enumerate(hFences):
        hset.add(hFence - 1)
        hset.add(m - hFence)

        for j in range(i):
            hset.add(abs(hFence - hFences[j]))

    maxEdge = -1

    if (n-1) in hset:
        return (n-1) ** 2 % MOD

    for i, vFence in enumerate(vFences):
        edge = vFence - 1
        if edge in hset and edge > maxEdge:
            maxEdge = edge

        edge = n - vFence
        if edge in hset and edge > maxEdge:
            maxEdge = edge

        for j in range(i):
            edge = abs(vFence - vFences[j])
            if edge in hset and edge > maxEdge:
                maxEdge = edge

    # print(hset, vset)
    
    if maxEdge == - 1:
        return -1
    else:
        return maxEdge ** 2 % MOD

m = 6
n = 7
hFences = [2]
vFences = [4]


m = 4
n = 3
hFences = [2,3]
vFences = [2]

m = 8
n = 5
hFences = [5,4]
vFences = [4]

print(solution(m,n, hFences, vFences))
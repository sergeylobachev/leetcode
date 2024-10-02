from math import inf

def solution(n, flights, src, dst, k):
    segments = k + 1
    al = [[] for _ in range(n)]

    for flight in flights:
        i, o, c = flight
        al[i].append((o, c))

    q = []

    distance = [inf] * n

    ## q will contain triplets (vertex, segments, path)
    distance[src] = 0
    q.append((src, 0, 0))

    while q:
        u, s, path = q.pop()
        if s < segments:
            for v in al[u]:
                dest, cost = v
                if path + cost < distance[dest]:
                    q.append((dest, s+1, path + cost))
                    distance[dest] = path + cost

    return distance[dst] if distance[dst] < inf else -1


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0


print(solution(n, flights, src, dst, k))
from collections import defaultdict
from collections import deque

def solution(n, connections):
    d = defaultdict(set)
    for a, b in connections:
        d[a].add((b, "outbound"))
        d[b].add((a, "inbound"))

    print("d[0] =", d[0])

    print(d)
    q = deque()
    processed = set()
    ans = 0
    q.append(0)
    while q:
        u = q.popleft()
        processed.add(u)
        for v, direction in d[u]:
            if v not in processed:
                if direction == "outbound":
                    ans += 1
                q.append(v)

    return ans


n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]

n = 3
connections = [[1,0],[2,0]]

print(solution(n, connections))

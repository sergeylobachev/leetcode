from collections import deque

def solution(n, edges):
    al = [[] for _ in range(n)]
    
    for a, b in edges:
        al[a].append(b)
        al[b].append(a)
    
    cc = 0
    
    visited = set()
    
    for i in range(n):
        if i not in visited:
            e_count = 0
            v_count = 0
            d = deque([i])
            while d:
                u = d.popleft()
                visited.add(u)
                v_count += 1
                e_count += len(al[u])
                for v in al[u]:
                    if v not in visited:
                        d.append(v)
            
            if e_count == v_count * (v_count - 1):
                cc += 1

    return cc

n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]

print(solution(n, edges))
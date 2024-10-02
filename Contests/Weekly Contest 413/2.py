from heapq import heappop
from heapq import heappush

def solution(queries, k):
    Q = len(queries)
    ans = [0] * Q

    h = []

    for i, (a, b) in enumerate(queries):
        d = abs(a) + abs(b)
        heappush(h, -d)
        if len(h) < k:
            ans[i] = -1
        elif len(h) == k:
            ans[i] = -h[0]
        else:
            heappop(h)
            ans[i] = -h[0]

    return ans

queries = [[1,2],[3,4],[2,3],[-3,0]]
k = 2

# queries = [[5,5],[4,4],[3,3]]
# k = 1

print(solution(queries, k))





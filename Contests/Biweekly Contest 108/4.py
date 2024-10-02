from collections import defaultdict
from collections import Counter

def solution(m, n, coordinates):
    R = m
    C = n
    a = defaultdict(int)

    for x, y in coordinates:
        if x > 0 and y > 0:
            a[(x-1, y-1)] += 1
        if x > 0 and y < C-1:
            a[(x-1, y)] += 1
        if x < R-1 and y > 0:
            a[(x, y-1)] += 1
        if x < R-1 and y < C- 1:
            a[(x,y)] += 1

    total = m * n
    vals = list(a.values())
    cnt = Counter(vals)

    return [(m-1)*(n-1) - len(vals), cnt[1], cnt[2], cnt[3], cnt[4]]


    
        
m = 3
n = 3
coordinates = [[0,0],[1,1],[0,2]]

print(solution(m, n, coordinates))
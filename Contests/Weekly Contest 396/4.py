from math import gcd
from collections import Counter


def solution(s):
    ctr = Counter(s)
    g = 0
    for v in ctr.values():
        g = gcd(g, v)
        
    return len(s) // g


s = "aabb"
print(solution(s))
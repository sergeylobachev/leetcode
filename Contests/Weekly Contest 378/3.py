from collections import defaultdict
import heapq

def solution(s):
    N = len(s)
    d = defaultdict(list)

    start = 0
    while start < N:
        letter = s[start]
        shift = 0
        while (start + shift) < N and s[start + shift] == letter:
            shift += 1
            d[letter].append(shift)
        start += shift
        
    ans = -1
    for key in d.keys():
        if len(d[key]) >= 3:
            ans = max(ans, min(heapq.nlargest(3, d[key])))

    return ans


s = "aaaa"
s = "abcdef"
s = "abcaba"
print(solution(s))
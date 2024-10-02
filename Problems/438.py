from collections import Counter

def solution(s, p):
    if len(s) < len(p):
        return []

    ans = []
    cntp = Counter(p)
    l = 0
    r = len(p)-1
    cnts = Counter(s[l:r+1])

    while True:
        if cnts == cntp:
            ans.append(l)
        
        cnts[s[l]] -= 1
        l += 1
        r += 1
        if r == len(s):
            return ans
        cnts[s[r]] += 1

    return ans





s = "cbaebabacd"
p = "abc"
print(solution(s, p))

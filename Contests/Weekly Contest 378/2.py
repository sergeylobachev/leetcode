from collections import defaultdict

def solution(s):

    N = len(s)
    d = defaultdict(int)
    
    for i in range(N):
        d[s[i]] += 1
        j = i + 1
        while j < N and s[j] == s[j-1]:
            j += 1
            d[s[i:j]] += 1

    ans = -1
    for key in d.keys():
        if d[key] >= 3:
            ans = max(ans, len(key))

    return ans


s = "aaaa"
# s = "abcdef"
# s = "abcaba"
print(solution(s))

from collections import Counter
from collections import defaultdict

def solution(s, k):
    best = 1
    l = 0
    r = 0
    d = defaultdict(int)
    d[s[0]] += 1

    while True:
        if max(d.values()) + k >= r - l + 1:  ## current window is good
            best = max(best, r-l+1)
            r += 1
            if r > len(s) - 1:
                return best
            d[s[r]] += 1

        else: ## current window is bad
            d[s[l]] -= 1
            l += 1

    return best







## Test Case 1, expected answer is 4
s = "ABAB"
k = 2
print(solution(s, k))

## Test Case 2, expected answer is 4
s = "AABABBA"
k = 1
print(solution(s, k))







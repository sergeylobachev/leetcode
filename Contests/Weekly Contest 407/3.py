from collections import Counter

def solution(s):
    N = len(s)

    ns = []
    ns.append(s[0])

    for i in range(1, N):
        if not (s[i] == "0" and s[i-1] == "0"):
            ns.append(s[i])

    N = len(ns)
    cnt = Counter(ns)
    zeros = cnt["0"]
    ans = 0
    for i in range(N):
        if ns[i] == "0":
            zeros -= 1
        else:
            ans += zeros

    return ans


    


s = "1001101"
s = "00111"
print(solution(s))

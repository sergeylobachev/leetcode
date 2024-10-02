
def solution(s, a, b, k):
    iInd = []
    jInd = []
    ans = []
    N = len(s)
    la = len(a)
    lb = len(b)

    for i in range(N):
        if i+len(a) <= N and s[i: i+len(a)] == a:
            iInd.append(i)

        if i + len(b) <= N and s[i: i+len(b)] == b:
            jInd.append(i)

    # print(iInd, jInd)
    for a in iInd:
        for b in jInd:
            if abs(a - b) <= k:
                ans.append(a)
                break
    
    ans.sort()
    return ans





s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15

print(solution(s, a, b, k))

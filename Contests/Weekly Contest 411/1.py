from collections import Counter

def solution(s, k):
    N = len(s)
    ans = 0
    
    for i in range(N):
        for j in range(i, N):
            l = s[i:j+1]
            print(l)
            cnt = Counter(l)
            if cnt["0"] <= k or cnt["1"] <= k:
                ans += 1
                
    return ans


s = "10101"
k = 1

s = "1010101"
k = 2

print(solution(s, k))

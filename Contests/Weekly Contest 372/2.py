def solution(s):
    N = len(s)
    ans = 0
    l = 0
    r = N - 1
    while l < r:
        if s[l] == "1" and s[r] == "0":
            ans += r - l
            l += 1
            r -= 1
        else:
            if s[l] == "0":
                l += 1
            if s[r] == "1":
                r -= 1
            
    return ans

s = "101"
print(solution(s))
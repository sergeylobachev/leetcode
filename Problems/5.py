
def solution(s):
    ans = ""
    maxlen = 1
    n = len(s)
    sNew = [0] * (2*n + 1)
    for i in range(0, 2*n+1, 2):
        sNew[i] = "|"
    for j in range(1, 2*n, 2):
        sNew[j] = s[j // 2]

    sNew = "".join(sNew)

    for center in range(1, 2*n):
        l = center - 1
        r = center + 1
        while l >= 0  and r <= 2*n:
            if sNew[l] == sNew[r]:
                curlen = r - l + 1
                if curlen >= maxlen:
                    maxlen = curlen
                    ans = sNew[l:r+1]
                l -= 1
                r += 1
            else: 
                break
        print(center, ans)
    

    ret = ""
    for char in ans:
        if char != "|":
            ret += char
    return ret





s = "cbbd"
print(solution(s))
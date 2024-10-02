from collections import Counter

def solution(s, t):

    lent = len(t)
    lens = len(s)

    cntt = Counter(t)
    cnts = Counter(s)

    if not cntt <= cnts:
        return ""
    
    cnts = Counter(s[0:lent])
    sumt = sum(cntt.values())
    sums = 0
    for elem in cntt.keys():
        sums += min(cntt[elem], cnts[elem])


    ans = [-1, -1]
    minlen = float("inf")

    l = 0
    r = lent-1

    while True:
        if sums < sumt:
            r += 1
            if r == lens:
                if ans == [-1, -1]:
                    return ""
                else:
                    return s[ans[0]: ans[1]+1]
            if cnts[s[r]] < cntt[s[r]]:
                sums += 1
            cnts[s[r]] += 1

        else:
            curlen = r - l + 1
            if curlen < minlen:
                minlen = curlen
                ans = [l, r]
            if cnts[s[l]] <= cntt[s[l]]:
                sums -= 1
            cnts[s[l]] -= 1
            l += 1

    
s = "ADOBECODEBANC"
t = "ABC"

# s = "a"
# t = "au"

print(solution(s, t))



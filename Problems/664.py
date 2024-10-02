from functools import cache

def solution(s):
    s = "*" + s
    news = ""
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            news += s[i]
    s = news

    ## resolves subproblem for [l, r]
    @cache
    def count(l, r):
        if l == r:
            return 1

        ans = 1
        ## left symbol
        symbol = s[l]
        l += 1
        start = l
        while l <= r:
            if s[l] == symbol:
                ans += count(start, l-1)
                start = l + 1
            l += 1
            if l > r and start <= r:
                ans += count(start, r)

        return ans

    return count(0, len(s)-1)


print(solution("ab"))
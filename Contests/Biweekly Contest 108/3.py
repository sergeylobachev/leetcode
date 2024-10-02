from functools import cache

def solution(s):

    powers = ["1", "101", "11001", "1111101", "1001110001", "110000110101", "11110100001001"]
    N = len(s)

    @cache
    def go(idx, prefix):
        if idx >= N and prefix == "":
            return 0

        if idx >= N and len(prefix) > 0:
            return 100

        ans = 0

        if (prefix + s[idx]) in powers:
            ans = min(1 + go(idx + 1, ""), go(idx + 1, prefix + s[idx]))
        else:
            ans = go(idx + 1, prefix + s[idx])

        return ans

    a = go(0, "")

    if a >= 100:
        return -1
    else:
        return a


s = "0"
print(solution(s))






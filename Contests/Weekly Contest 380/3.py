def solution(k, x):

    def calc(n):
        p = 0 ## position
        ans = 0

        while n >= 2 ** p:
            if (p + 1) % x == 0:
                full = (n + 1) // (2 ** (p+1))
                part = (n + 1) % (2 ** (p+1))
                cur = full * 2 ** p + max(0, part-2**p)
                ans += cur
            p += 1

        return ans

    l = 1
    r = 10 ** 15
    while l <= r:
        m = (l + r) // 2
        if calc(m) <= k:
            l = m + 1
        else:
            r = m - 1

    return l-1


k = 9
x = 1


k = 7
x = 2

print(solution(k, x))



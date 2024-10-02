from math import lcm

def solution(n, a, b, c):
    ab = lcm(a, b)
    bc = lcm(b, c)
    ca = lcm(c, a)
    abc = (lcm(a, lcm(b, c)))

    def helper(k):
        return k // a + k // b + k // c - (k // ab + k // bc + k //ca) + k // abc

    l = 0
    r = 10 ** 20

    while l < r-1:
        m = (l + r) // 2
        if helper(m) < n:
            l = m
        if helper(m) >= n:
            r = m

    return l + 1

print(solution(5, 2, 11, 13))
def solution(n):
    l = 0
    r = n

    while l <= r:
        m = (l + r) // 2
        print(m)
        if m * (m+1) // 2 <= n < (m+1)*(m+2) // 2:
            return m
        elif n < m * (m+1) // 2:
            r = m - 1
        else:
            l = m + 1

print(solution(8))
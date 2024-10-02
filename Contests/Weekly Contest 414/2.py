def solution(start, d):

    N = len(start)
    start.sort()
    l = 0
    r = 10 ** 20
    for i in range(1, N):
        r = min(r, d + start[i] - start[i-1])


    def can(n):
        cur = start[0]
        for i in range(1, N):
            cur = max(start[i], cur + n)
            if cur > start[i] + d:
                return False

        return True

    for i in range(10):
        print(f"i ={i}, can= {can(i)}")

    ans = 0

    while l <= r:
        m = (l + r) // 2
        if can(m):
            ans = m
            l = m + 1
        else:
            r = m - 1

    return ans

start = [2,6,13,13]
d = 5

# start = [6,0,3]
# d = 2

print(solution(start, d))
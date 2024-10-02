def solution(colors, k):
    N = len(colors)
    c = colors + colors

    cur = c[0]
    curlen = 1
    ans = 0

    print(c)

    for i in range(1, 2*N):
        if c[i] != cur:
            curlen += 1
            cur = c[i]

        else:
            cur = c[i]
            curlen = 1

        if curlen >= k and i - k < N-1:
            ans += 1

    return ans


colors = [0,1,0,1,0]
k = 3

# colors = [0,1,0,0,1,0,1]
# k = 6

# colors = [1,1,0,1]
# k = 4

# colors = [0, 1, 0, 1]
# k = 3

print(solution(colors, k))

from collections import defaultdict

def solution(points, s):

    N = len(points)
    radius = 10 ** 10

    d = defaultdict(int)

    for i, c in enumerate(s):
        curdist = max(abs(points[i][0]), abs(points[i][1]))
        if c not in d:
            d[c] = curdist
        else:  # c in dictionary
            if curdist == d[c]:
                radius = min(radius, curdist-1)
            else:
                radius = min(radius, max(d[c], curdist) - 1)
                d[c] = min(curdist, d[c])

        print(i, radius, c, d)


    ans = 0
    for i in range(N):
        curdist = max(abs(points[i][0]), abs(points[i][1]))
        if curdist <= radius:
            ans += 1

    return ans
                




points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]
s = "abdca"

# points = [[1,1],[-2,-2],[-2,2]]
# s = "abb"

# points = [[1,1],[-1,-1],[2,-2]]
# s = "ccd"

# points = [[16,32],[27,3],[23,-14],[-32,-16],[-3,26],[-14,33]]
# s = "aaabfc"

# points = [[10,-12],[-5,-4],[-7,15],[9,16]]
# s = "dada"

# points = [[-28,33],[12,-38],[13,-9],[-17,42],[-37,42],[8,35],[11,43]]
# s = "ggcbbbf"

points = [[-54,27],[17,39],[26,-57],[-32,-61],[-54,59],[-46,60],[-18,-63],[45,26]]
s = "aebffcee"


print(solution(points, s))



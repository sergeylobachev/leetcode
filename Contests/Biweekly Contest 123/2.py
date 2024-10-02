

def solution(points):
    ans = 0
    N = len(points)

    for a in range(N):
        for b in range(N):
            if a == b: 
                continue
            ax, ay = points[a][0], points[a][1]
            bx, by = points[b][0], points[b][1]
            if ax > bx or ay < by:
                continue
            flag = 1
            for c in range(N):
                if c == a or c == b:
                    continue
                cx, cy = points[c][0], points[c][1]
                if (ax <= cx <= bx) and (ay >= cy >= by):
                    flag = 0

            if flag:
                print(a,b)
                ans += 1

    return ans


points = [[1,1],[2,2],[3,3]] # 0
# points = [[6,2],[4,4],[2,6]] # 2
# points = [[3,1],[1,3],[1,1]] # 2

print(solution(points))

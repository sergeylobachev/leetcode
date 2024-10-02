# points = [[2,1],[1,0],[1,4],[1,8],[3,5],[4,6]]
# w = 1

points = [[2,3],[1,2]]
w = 0

# points = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
# w = 2

def solution(points, w):
    x = [0] * len(points)

    for i in range(len(points)):
        x[i] = points[i][0]

    x = list(set(x))
    s = sorted(x)

    answer = 0
    b = -1
    for i in range(len(s)):
        if s[i] > b:
            b = s[i] + w
            answer += 1

    return answer

print(solution(points, w))

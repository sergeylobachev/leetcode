from collections import deque

def solution(positions, healths, directions):
    N = len(positions)
    robots = [0] * N

    ## don't forget to map later
    for i in range(N):
        robots[i] = [positions[i], healths[i], directions[i], i]

    robots.sort()

    l = deque()
    r = deque()

    # print(robots)

    for p, h, d, i in robots:
        if d == "R":
            while len(l) > 0 and h > 0:
                if h == l[-1][1]:
                    h = 0
                    l.pop()
                elif h > l[-1][1]:
                    l.pop()
                    h -=1
                else:
                    h = 0
                    l[-1][1] -= 1

            if h > 0:
                r.append([p, h, d, i])

        if d == "L":
            while len(r) > 0 and h > 0:
                if h == r[-1][1]:
                    h = 0
                    r.pop()
                elif h > r[-1][1]:
                    r.pop()
                    h -=1
                else:
                    h = 0
                    r[-1][1] -= 1

            if h > 0:
                l.append([p, h, d, i])

    # print(f"l={l}")
    # print(f"r={r}")

    survived = list(l + r)
    survived.sort(key = lambda x: x[3])
    
    return [x[1] for x in survived]


positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"

positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"

print(solution(positions, healths, directions))
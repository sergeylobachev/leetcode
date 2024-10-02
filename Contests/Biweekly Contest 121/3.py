from collections import defaultdict

def solution(x, y):

    q = []
    visited =set()
    q.append((x,0))

    while q:
        element, distance = q.pop(0)
        if element == y:
            return distance
        if element in visited:
            pass
        else:
            visited.add(element)
            q.append((element-1, distance+1))
            q.append((element+1, distance+1))
            if element % 5 == 0:
                q.append((element // 5, distance+1))
            if element % 11 == 0:
                q.append((element // 11, distance+1))

x = 26
y = 1

x = 54
y = 2

print(solution(x, y))
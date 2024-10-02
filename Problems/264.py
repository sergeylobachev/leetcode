from collections import deque

def solution(n):
    two = deque([1])
    three = deque([1])
    five = deque([1])

    counter = 0

    while counter < n:
        current = min(two[0], three[0], five[0])
        counter += 1
        if two[0] == current:
            two.popleft()
        if three[0] == current:
            three.popleft()
        if five[0] == current:
            five.popleft()
        two.append(current * 2)
        three.append(current*3)
        five.append(current*5)

    return current


print(solution(1))








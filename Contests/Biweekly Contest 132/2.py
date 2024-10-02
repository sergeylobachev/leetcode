from collections import deque

def solution(skills, k):
    N = len(skills)
    print(q)
    cur_winner = q[0]
    cur_index = 0
    counter = 0
    el_counter = 0

    while counter < k and el_counter < N+1:
        el_counter += 1
        first = q.popleft()
        second = q.popleft()
        if first > second:
            counter += 1
            q.append(second)
            q.appendleft(first)
            cur_winner = first

        else:
            counter = 1
            q.append(first)
            q.appendleft(second)
            cur_winner = second


    for idx, player in enumerate(skills):
        if player == cur_winner:
            return idx


skills = [4,2,6,3,9]
k = 2

skills = [2,5,4]
k = 3

print(solution(skills, k))



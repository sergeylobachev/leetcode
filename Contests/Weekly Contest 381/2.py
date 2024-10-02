from collections import Counter


def solution(n, x, y):
    x -= 1
    y -= 1
    distances = []
    answer = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            a = min(abs(i-j), 1 + abs(i-min(x,y)) + abs(j-max(x,y)))
            distances.append(a)

    cnt = Counter(distances)
    for k in range(n):
        answer[k] = cnt[k+1] * 2

    print(answer)


solution(3,1,3)
solution(3,3,1)
solution(5,2,4)
solution(4,1,1)



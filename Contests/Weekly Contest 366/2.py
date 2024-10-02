def solution(p, t):
    p.sort()
    t.sort(reverse = True)

    answer = 0
    tidx = 0
    for i in range(0, len(p)):
        for j in range(4):
            answer = max(answer, p[i] + t[tidx])
            tidx += 1

    return answer


p = [8,10]
t = [2,2,3,1,8,7,4,5]

p = [10,20]
t = [2,3,1,2,5,8,4,3]

print(solution(p, t))
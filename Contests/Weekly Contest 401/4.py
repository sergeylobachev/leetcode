def solution(R):
    a = 1
    R.sort()
    for r in R:
        mask = 2 ** r - 1
        t = (a & mask) << r
        a = a | t

    answer = 0
    for i in range(10000):
        if a & 1:
            answer = i
        a >>= 1

    return answer



R = [1,1,3,3]
R = [1,6,4,3,2]
print(solution(R))
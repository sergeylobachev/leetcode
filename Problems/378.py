def index(matrix, num):
    l = len(matrix)
    lb = 0
    rb = 0
    for i in range(l):
        for j in range(l):
            if matrix[i][j] < num:
                lb += 1
            if matrix[i][j] == num:
                rb += 1

    if rb:
        return lb + 1, lb + rb
    else:
        return lb + 1, lb + 1


def solution(matrix, k):
    # l = - 10 ** 9 
    # r = 10 ** 9

    l = 1
    r = 15

    while l <= r:
        m = (l + r) // 2
        lb, rb = index(matrix, m)
        if lb <= k <= rb:
            return m
        elif k > rb:
            r = m - 1
        else:
            l = m + 1

    return -1

matrix = [[1,5,9],[10,11,13],[12,13,15]]
num = 13
k = 8

print(index(matrix, 8))
# print(solution(matrix, k))
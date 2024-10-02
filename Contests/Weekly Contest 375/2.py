def solution(variables, target):

    ans = []
    for idx, (a, b, c, m) in enumerate(variables):
        res = 1
        for i in range(b):
            res = (res * a) % 10
            print(res)
        print()

        newres = 1
        for j in range(c):
            newres = (newres * res) % m
            print(newres)

        if newres == target:
            ans.append(idx)

    return ans

variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
target = 2

variables = [[39,3,1000,1000]]
target = 17

print(solution(variables, target))
def solution(left, right):
    return sum( sum(list(map(lambda x: int(x), str(s)))[:len(str(s)) // 2]) == sum(list(map(lambda x: int(x), str(s)))[len(str(s)) // 2:])
and len(str(s)) % 2 == 0 for s in range(left, right+1))


# s = 123456
# str = str(s)

# leftsum = sum(list(map(lambda x: int(x), str))[:len(str) // 2])
# rightsum = sum(list(map(lambda x: int(x), str))[len(str) // 2:])
# print(leftsum, rightsum)






print(solution(1200, 1230))

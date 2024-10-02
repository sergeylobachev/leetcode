def can(stones, j):

    l = r = stones[0]
    counter = 0

    if j >= stones[-1] - stones[0]:
        return True

    while r < j:
        r += 1
        if r in s:
            counter += 1

    if counter < 2:
        return False

    while r <= stones[-1] - 1:
        if l in s:
            counter -= 1
        l += 1
        r += 1
        if r in s:
            counter += 1

        if counter < 2:
            return False

    return True


stones = [0,5,9,10,21]
s = set(stones[1:len(stones)-1])
print(s)


for i in range(21):
    print(i, can(stones, i))




# l = 0
# r = stones[-1]

# while l <= r:
#     mid = (l + r) // 2
#     if can(stones, mid):
#         r = mid - 1
#     else:
#         l = mid + 1

#     return l-1


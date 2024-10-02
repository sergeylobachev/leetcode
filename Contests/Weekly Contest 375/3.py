# from collections import defaultdict


def solution(nums, k):

    N = len(nums)
    maxElem = max(nums)
    roll = [0] * N
    ans = 0
    counter = 0
    d = {}

    for idx, num in enumerate(nums):
        roll[idx] = counter
        if num == maxElem:
            counter += 1
            d[counter] = idx

    print(roll, d)

    for idx, num in enumerate(roll):
        if (num + k) in d:
            ans += N - d[num+k]

    return ans


nums = [1,3,2,3,3]
k = 2

nums = [1,4,2,1]
k = 3

print(solution(nums, k))




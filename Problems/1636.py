from collections import Counter


def solution(nums):
    N = len(nums)
    d = Counter(nums)
    l = list(d.items())
    l.sort(key = lambda x: (x[1], -x[0]))

    answer = [0] * N
    i = 0
    for num, freq in l:
        for j in range(freq):
            answer[i] = num
            i += 1

    return answer



nums = [1, 2, 2, 3, 3, 3, 4, 4]
print(solution(nums))
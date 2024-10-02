from collections import Counter

def solution(nums):
    l = len(nums)
    cnt = Counter(nums)
    answer = [0 for _ in range(l - len(cnt.keys()))]
    k = 0
    for i in range(1, l+1):
        if i not in cnt.keys():
            answer[k] = i
            k += 1

    return answer

nums = [1,1]

print(solution(nums))
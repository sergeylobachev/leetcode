from collections import Counter

def solution(nums):
    cnt = Counter(nums)
    ans = 0
    for c in cnt:
        if cnt[c] == 2:
            ans ^= c

    return ans

nums = [1,2,1,3]
nums = [1,2,3]
nums = [1,2,2,1]

print(solution(nums))
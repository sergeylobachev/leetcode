from collections import Counter

nums = [1,2,3,1,1,3]

def solution(nums):
    ans = 0
    cnt = Counter(nums)
    print(cnt, cnt.values())
    for count in cnt.values():
        ans += count * (count - 1) // 2
    return ans

print(solution(nums))
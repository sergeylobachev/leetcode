from collections import Counter

def solution(nums):
    N = len(nums)
    K = len(str(nums[0]))

    nums = [str(num) for num in nums]
    ans = 0

    # for i in range(K):

    for i in range(K):
        cnt = Counter(num[i] for num in nums)
        for c in cnt:
            ans += cnt[c] * (N-cnt[c])

    return ans // 2


nums = [10,10,10,10]
nums = [13,23,12]
print(solution(nums))



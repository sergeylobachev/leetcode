from collections import defaultdict

def solution(nums):
    N = len(nums)
    d = defaultdict(int)
    ans = 0

    d[nums[0]] = 1
    d[nums[1]] = 1

    for i in range(2, N):
        l = 1
        for j in range(i):
            if (nums[i] - nums[j]) in d and nums[i] - nums[j] < nums[j]:
                l = max(l, d[nums[i] - nums[j]] + 2)
                ans = max(ans, l)

            d[nums[i]] = l
            
    print(d)
    return ans if ans > 2 else 0



nums = [1,2,3,4,5,6,7,8]
nums = [1,3,7,11,12,14,18]
nums = [2,4,5,6,7,8,11,13]
print(solution(nums))
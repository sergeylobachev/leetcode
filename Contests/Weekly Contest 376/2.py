
def solution(nums, k):
    nums.sort()
    N = len(nums)
    ans = [] * N

    idx = 0

    while idx + 3 <= N:
        if nums[idx+2] - nums[idx] > k:
            return []
        ans.append(nums[idx:idx+3])
        idx += 3

    return ans

nums = [1,3,4,8,7,9,3,5,1]
k = 2


nums = [1,3,3,2,7,3]
k = 3

print(solution(nums, k))



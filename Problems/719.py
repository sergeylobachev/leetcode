def at_least_k(nums, target):
    count = 0
    l = 0

    for i in range(len(nums)):
        while nums[i] - nums[l] > target:
            l += 1
        count += i - l

    return count >= k



def solution(nums, k):
    nums.sort()
    l = 0
    r = nums[-1]

    while l < r:
        m = (l + r) // 2
        if at_least_k(nums, m):
            r = m
        else:
            l = m + 1

    return r



nums = [1,3,1,5]
k = 1

nums = [1,6,1]
k = 3

# nums = [1,1,1]
# k = 2

print(solution(nums, k))



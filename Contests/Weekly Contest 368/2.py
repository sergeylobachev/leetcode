def solution(nums):
    n = len(nums)

    l = [10**9] * n
    r = [10**9] * n
    
    ml = nums[0]
    for i in range(1, n):
        l[i] = ml
        ml = min(ml, nums[i])

    mr = nums[-1]
    for i in range(n-2, -1, -1):
        r[i] = mr
        mr = min(mr, nums[i])

    ans = 10 ** 9
    for i in range(1, n-1):
        if nums[i] > l[i] and nums[i] > r[i]:
            ans = min(ans, nums[i] + l[i] + r[i])

    if ans >= 10 ** 9:
        return -1
    else: return ans

nums = [5,4,8,7,10,2]
nums = [6,5,4,3,4,5]
print(solution(nums))

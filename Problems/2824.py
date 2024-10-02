def bs(l, r, target):
    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m -1
    return l

def solution(nums, target):
    nums.sort()
    print(nums)
    answer = 0

    for i in range(len(nums)-1):
        l = i + 1
        r = len(nums) - 1
        t = target - nums[i]
        answer += bs(l, r, t) - i -1

    return answer


nums = [-1,1,2,3,1]
target = 2

print(solution(nums, target))
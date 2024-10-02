def solution(nums):

    nums.sort()
    ans = 0
    N = len(nums)

    if nums[0] = 0:
        ans += 1

    for i in range(N):
        if i + 1 > nums[i]:
            if i + 1 < N and nums[i+1] <= i + 1:
                continue
            ans += 1

    return ans


nums = [6,0,3,3,6,7,2,7]
nums = [1,1]
print(solution(nums))
def solution(nums):
    N = len(nums)
    ans = 0
    for i in range(N-2):
        if nums[i] == 0:
            ans += 1
            nums[i] = 1 - nums[i]
            nums[i+1] = 1 - nums[i+1]
            nums[i+2] = 1 - nums[i+2]

    if nums[N-1] == nums[N-2] == 1:
        return ans
    else: return -1


nums = [0,1,1,1,0,0]
nums = [0,1,1,1]
print(solution(nums))

def solution(nums):
    N = len(nums)
    s = nums[0]
    
    for i in range(N-1):
        if nums[i] == nums[i+1] - 1:
            s += nums[i+1]
        else:
            break


    while True:
        if s not in nums:
            return s
        s += 1


nums = [1,2,3,2,5]
nums = [3,4,5,1,12,14,13]
nums = [4,5,6,7,8,8,9,4,3,2,7]
print(solution(nums))
def solution(nums):
    flips = 0
    N = len(nums)

    for i in range(N):
        if (nums[i] == 0 and flips % 2 == 0) or (nums[i] == 1 and flips % 2):
            flips += 1

    return flips
        
nums = [0,1,1,0,1]
nums = [1,0,0,0]
print(solution(nums))
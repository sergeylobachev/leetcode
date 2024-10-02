from collections import deque

def solution(nums, m):
    N = len(nums)

    for i in range(1, N):
        if nums[i] + nums[i-1] >= m:
            return True
        
    return False


# nums = [2, 2, 1]
# m = 4

nums = [4, 1, 3, 2, 4]
m = 6


print(solution(nums, m))



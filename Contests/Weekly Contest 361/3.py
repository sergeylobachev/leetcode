from collections import defaultdict

def solution(nums, modulo, k):

    N = len(nums)

    for idx, num in enumerate(nums):
        if num % modulo == k:
            nums[idx] = 1
            roll += 1
            d[roll] = idx
        else:
            nums[idx] = 0

    for i in range(N):
        

    print(nums, d)

    
nums = [3,1,9,6]
modulo = 3
k = 0

print(solution(nums, modulo, k))

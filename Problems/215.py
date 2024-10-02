import heapq

def solution(nums, k):    
    N = len(nums)
    h = nums[:k]
    heapq.heapify(h)

    for i in range(k, N):
        if nums[i] > h[0]:
            heapq.heapreplace(h, nums[i])

    return h[0]


nums = [3,2,1,5,6,4]
k = 2

print(solution(nums, k))
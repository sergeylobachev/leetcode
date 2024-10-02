from collections import deque

def solution(nums, k):
    ans = []
    d = deque()

    for i in range(k):
        while d and d[-1][0] <= nums[i]:
            d.pop()
        d.append([nums[i], i])
    
    ans.append(d[0][0])

    for i in range(k, len(nums)):
        if d[0][1] <= i-k:
            d.popleft()
        while d and d[-1][0] <= nums[i]:
            d.pop()

        d.append([nums[i], i])
        ans.append(d[0][0])

    return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(solution(nums, k))

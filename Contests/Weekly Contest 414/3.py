from collections import deque

def solution(nums):

    N = len(nums)
    ans = 0
    q = deque()

    nums = nums[::-1]

    for i in range(1, N):
        while len(q) > 0 and q[-1][1] <= nums[i]:
            q.pop()
        q.append([i, nums[i]])

    q.appendleft([0,0])
    # print(q)
    
    for i in range(1, len(q)):
        ans += q[i][1] * (q[i][0] - q[i-1][0])

    return ans
   
nums = [1,3,1,5]
# nums = [4,3,1,3,2]
print(solution(nums))
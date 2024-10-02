from collections import defaultdict

def solution(nums, k):
    N = len(nums)
    d = defaultdict(int)
    ans = 0
    d[0] = 1
    roll = 0
    for num in nums:
        roll = (roll + num) % k
        ans += d[roll] 
        d[roll] += 1
    
    return ans
    




nums = [4,5,0,-2,-3,1]
k = 5

nums = [5]
k = 9

print(solution(nums, k))


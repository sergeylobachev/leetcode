from collections import defaultdict

def solution(nums, k):
    d = defaultdict(int)
    N = len(nums)
    l = 0
    ans = 0
    
    for i in range(N):
        d[nums[i]] += 1
        while d[nums[i]] > k:
            d[nums[l]] -= 1
            l += 1

        ans = max(ans, i-l+1)
        
    return ans

# nums = [1,2,3,1,2,3,1,2]
# k = 2

nums = [1,2,1,2,1,2,1,2]
k = 1

print(solution(nums, k))
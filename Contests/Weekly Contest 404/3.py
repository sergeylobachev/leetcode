from collections import Counter
from collections import defaultdict

def solution(nums, k):
    N = len(nums)
    ans = 0
    nums = [x % k for x in nums]

    for rem in range(k):
        d = defaultdict(int)
        for i in range(N):
            d[nums[i]] = d[(rem - nums[i]) % k] + 1

        ans = max(ans, max(d.values()))

    return ans
        
    


nums = [1,2,3,4,5]
k = 2



# nums = [1,4,2,3,1,4]
# k = 3

print(solution(nums, k))
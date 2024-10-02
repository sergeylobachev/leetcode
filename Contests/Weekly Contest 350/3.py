from collections import defaultdict
from functools import cache

def solution(nums):
    N = len(nums)
    MOD = 10 ** 9 + 7
    adj = defaultdict(list)

    for i in range(N):
        for j in range(N):
            if (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0) and i != j:
                adj[nums[i]].append(nums[j])
                adj[1].append(nums[i])

    print(adj)
                
    @cache
    def bfs(last, left):
        if len(left) == 0:
            return 1
        
        ans = 0
        for l in left:
            if l in adj[last]:
                lcopy = tuple(item for item in left if item != l)
                ans += bfs(l, lcopy)
        
        return ans % MOD
        

    return bfs(1, tuple(nums))


print(solution([1,4,3]))
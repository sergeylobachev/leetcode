from collections import Counter
from collections import defaultdict


def solution(nums, k):
    N = len(nums)
    dp = [[0] * (k+1) for _ in range(N)]

    ans = 1

    for i in range(N):
        dp[i][0] = 1
        for j in range(k+1):
            for l in range(i):
                if nums[l] == nums[i]:
                    dp[i][j] = max(dp[i][j], dp[l][j]+1)
                if j > 0 and nums[l] != nums[i]:
                    dp[i][j] = max(dp[i][j], dp[l][j-1] + 1)

            ans = max(ans, dp[i][j])

    return ans



    
nums = [1,2,1,1,3]
k = 2

nums = [1,2,3,4,5,1]
k = 0

print(solution(nums, k))
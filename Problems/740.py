from collections import Counter

nums = [1]

def solution(nums):
    arr = [0] * (max(nums) + 1)
    cnt = Counter(nums)
    for key in cnt.keys():
        arr[key] = key * cnt[key]

    dp = [0] * len(arr)
    dp[1] = arr[1]
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2] + arr[i], dp[i-1])
    
    return dp[-1]








print(solution(nums))
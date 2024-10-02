def solution(nums, target):
    dp = [-1] * (target+1)
    dp[0] = 0

    
    for num in nums:
        for i in range(target, -1, -1):
            if i - num >= 0 and dp[i-num] > -1:
                dp[i] = max(dp[i], dp[i-num] + 1)
            


    return dp[-1]




nums = [1,2,3,4,5]
target = 9

nums = [4,1,3,2,1,5]
target = 7

nums = [1,1,5,4,5]
target = 3

print(solution(nums, target))
# nums = [3,2,1,2,3,4]
# nums = [3,2,6,1,4]
# nums = [3, 8, 8]
nums = [1,1,2,3,2,2,1,3,3]

def helper(nums, n):
    l = len(nums)
    dp = [[0] * l for i in range(l)]
    for k in range(1, l):
        for i in range(l-k):

            dp[i][i+k] = k
            # a = 0
            # b = 0
            # c = 0
            # if nums[i] + nums[i+1] == n:
            #     a = 1 
            #     if i+2 <= l- 1:
            #         a += dp[i+2][i+k]

            # if nums[i+k-1] + nums[i+k] == n:
            #     b += 1
            #     if i+k-2 >= 0 :
            #         b += dp[i][i+k-2]

            # if nums[i] + nums[i-k] == n:
            #     c += 1
            #     if i+1 <= l-1  and i+k-1 >= 0:
            #         c = dp[i+1][i+k-1]

            # dp[i][i+k] = max(a, b, c)
        k += 1
    print(dp)
    return dp[0][-1]

def solution(nums):
    if len(nums) == 2:
        return 1

    l = len(nums)
    start = helper(nums[2::], nums[0] + nums[1])
    # print(f"start, {nums[2::]}", {nums[0] + nums[1]})
    # print(f"start= , {start}")

    edges = helper(nums[1:l-1], nums[0] + nums[l-1])
    # print(f"adges, {nums[1:l-1]}, {nums[0] + nums[l-1]}")
    # print(f"edges= , {edges}")

    end = helper(nums[:l-2], nums[l-2] + nums[l-1])
    # print(f"end, {nums[:l-2]}, {nums[l-2] + nums[l-1]}")
    # print(f"end={end}")

    return 1 + max(start, edges, end)


print(helper(nums, 4))
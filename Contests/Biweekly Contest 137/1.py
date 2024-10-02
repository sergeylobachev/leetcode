def solution(nums, k):
    ans = []
    N = len(nums)
    l = 0

    for i in range(N):
        if i > 0 and nums[i] == nums[i-1] + 1:
            l += 1
        else:
            l = 1

        if i >= k-1:
            if l >= k:
                ans.append(nums[i])
            else:
                ans.append(-1)

    return ans


nums = [1,2,3,4,3,2,5]
k = 3

# nums = [2,2,2,2,2]
# k = 4

# nums = [3,2,3,2,3,2]
# k = 2

print(solution(nums, k))

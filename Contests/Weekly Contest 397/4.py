def calc(nums, perm):
    N = len(nums)
    ans = 0
    for i in range(N):
        ans += abs(perm[i] - nums[perm[(i+1) % N]])


    return ans

nums = [1, 0, 2]
perm = [2, 1, 0]

print(calc(nums, perm))




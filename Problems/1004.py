nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


def can(nums, n, k):

    zeroes = 0
    l = 0
    r = n - 1
    for i in range(n):
        if nums[i] == 0:
            zeroes += 1
    if zeroes <= k:
        return True

    

    while r < len(nums) - 1:
        if nums[l] == 0:
            zeroes -= 1
        l += 1
        r += 1
        if nums[r] == 0:
            zeroes += 1
        if zeroes <= k:
            return True

    return False


print(can(nums, 4, 0))




# l = 0
# r = len(nums)

# while l <= r:
#     m = (l + r) // 2
#     if can(nums, m, k):
#         r =  m + 1
#     else:
#         l = m - 1

# return l + 1
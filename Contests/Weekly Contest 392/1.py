nums = [2, 3,3,3]

def solution(nums):
    l = 0
    r = 1
    maxlen = 1

    while l < len(nums):
        while r < len(nums) and nums[r] > nums[r-1]:
            maxlen = max(maxlen, r-l+1)
            r += 1
        l = r
        r += 1

    l = 0
    r = 1

    while l < len(nums):
        while r < len(nums) and nums[r] < nums[r-1]:
            maxlen = max(maxlen, r-l+1)
            r += 1
        l = r
        r += 1

    return maxlen





print(solution(nums))

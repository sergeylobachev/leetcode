
def solution(nums):
    N = len(nums)
    ones = 0
    zeroes = 0
    for i in range(N):
        if nums[i] % 2 == 0:
            zeroes += 1
        else:
            ones += 1

    mixed = 1
    cur = nums[0] % 2
    for i in range(1, N):
        if nums[i] % 2 != cur:
            mixed += 1
            cur = abs(1 -cur)

    return max(ones, zeroes, mixed)


nums = [1,2,3,4]
nums = [1,2,1,1,2,1,2]
nums = [1,3]

print(solution(nums))
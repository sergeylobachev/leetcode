def solution(nums, id, vd):
    N = len(nums)

    max_i = 0
    min_i = 0
    for i in range(id, N):
        if nums[i-id] > nums[max_i]:
            max_i = i-id
        if nums[i-id] < nums[min_i]:
            min_i = i-id
        if abs(nums[i] - nums[max_i]) >= vd:
            return [max_i, i]
        if abs(nums[i] - nums[min_i]) >= vd:
            return [min_i, i]

    return [-1, -1]


nums = [5,1,4,1]
id = 2
vd = 4

nums = [2,1]
id = 0
vd = 0

nums = [1,2,3]
id = 2
vd = 4

print(solution(nums, id, vd))
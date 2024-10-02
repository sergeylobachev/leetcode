def solution(nums, energy):
    points = 0
    nums.sort()
    l = 0

    if energy < nums[0]:
        return 0
    
    energy += sum(nums) - nums[0]

    return energy // nums[0]
    

# nums = [3,2,2]
# energy = 2  


# nums = [2]
# energy = 10

nums= [2, 3, 4]
energy = 1

print(solution(nums, energy))
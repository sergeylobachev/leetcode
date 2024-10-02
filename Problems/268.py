nums = [0,1]

def solution(nums):
    d = {}
    for num in nums:
        d[num] = 1
    for i in range(len(nums)):
        if i not in d.keys():
            return i

    return len(nums)

print(solution(nums))
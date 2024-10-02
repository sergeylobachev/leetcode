nums = [5,7,0]
changeIndices = [1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]


def isOK(steps, nums, changeIndices):
    n = len(nums)
    visited = set()
    ops = 0
    for i in range(steps-1, -1, -1):
        j = changeIndices[i]
        if j not in visited:
            ops += nums[j-1]
            visited.add(j)
        elif ops:
            ops -= 1
    if len(visited) < n: return False
    return ops == 0
def match(nums, pattern, start):
    p = len(pattern)
    a = []
    for i in range(start+1, start+1+p):
        if nums[i] > nums[i-1]:
            a.append(1)
        elif nums[i] == nums[i-1]:
            a.append(0)
        else:
            a.append(-1)
    print(a)
    return a == pattern

def solution(nums, pattern):
    ret = 0
    N = len(nums)
    P = len(pattern)
    for i in range(N-P):
        ret += match(nums, pattern, i)

    return ret




# nums = [1,2,3,4,5,6]
# pattern = [1,1]

nums = [1,4,4,1,3,5,5,3]
pattern = [1,0,-1]

print(match(nums, pattern, 0))
print(solution(nums, pattern))

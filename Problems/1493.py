# nums = [1,1,0,1]
nums = [0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1]
# nums = [1,1,1]

def solution(nums):
    l = 0
    r = 0
    z = 0
    a = 0
    counter = 0
    while r < len(nums):
        while z < 2 and r < len(nums):
            if nums[r] == 0:
                z += 1
            r += 1
            counter += 1
        a = max(a, counter-2) if z == 2 else max(a, counter-1)
        while z > 1:
            if nums[l] == 0:
                z -= 1
            l += 1
            counter -= 1

    return a

def solution2(nums):
    k = 1
    i = 0
    for j in range(len(nums)):
        k -= nums[j] == 0
        if k < 0:
            k += nums[i] == 0
            i += 1

    print(f"i={i}, j={j}")
    return j - i



print(solution2(nums))


def solution(nums):
    l = len(nums)
    sum = 0
    for i in range(2 ** l):
        elem = 0
        for j in range(l):
            if i & (1 << j):
                elem ^= nums[j]

        sum += elem
    return sum


# for mask in range(1 << 14):
#     print(mask)
print(1 << 8)
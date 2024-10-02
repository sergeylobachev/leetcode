from math import inf

def solution(nums, k):
    roll = [inf] * 32
    ans = 10 ** 9

    for idx, num in enumerate(nums):
        num = format(num, "#034b")[2:]
        for i in range(32):
            if num[~i] == "0":
                roll[~i] = inf
            elif roll[~i] == inf:
                roll[~i] = idx

        print(roll[::-1])

        l = sorted(set(roll))
        print(l)
        if l[0] != 0:
            ans = min(ans, k)

        candidate = 0
        for item in l:
            if item != inf:
                for pos in range(32):
                    if roll[::-1][pos] == item:
                        candidate |= 1 << pos
                ans = min(ans, abs(candidate - k))
        
    return ans

        
        
nums = [1,2,4,5]
k = 3

nums = [1,2,1,2]
k = 2

nums = [1]
k = 10

nums = [56,46,80,58,56]
k = 1

nums = [6]
k = 2

print(solution(nums, k))
            

















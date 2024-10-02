import copy

def solution(nums):
    N = len(nums)
    ans = 0

    a = []
    
    for i in range(N):
        for j in range(i, N):
            new = nums[:i] + nums[j+1:]
            a.append(new)

    for new in a:
        if len(new) == 0 or len(new) == 1:
            ans += 1
        else:
            for i in range(1, len(new)):
                if new[i] <= new[i-1]:
                    break
            else:
                ans += 1

    return ans

nums = [1,2,3,4]
# nums = [6,5,7,8]
nums = [8,7,6,6]

print(solution(nums))
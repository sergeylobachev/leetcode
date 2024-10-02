def solution(nums):
    N = len(nums)
    # sos -- sum of scores
    sos = nums[0] 
    for i in range(1, N):
        sos &= nums[i]
    
    if sos > 0:
        return 1
    

    ans = 0
    i = 0
    while i < N:
        cts = nums[i]
        while cts != 0:
            i += 1
            if i == N:
                return ans
            cts &= nums[i]

        ans += 1
        i += 1

    return ans


nums = [1,0,2,0,1,2]
# nums = [5,7,1,3]
nums = [22,21,29,22]
print(solution(nums))
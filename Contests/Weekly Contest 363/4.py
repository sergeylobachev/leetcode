def solution(nums):

    N = len(nums)
    answer = 0

    for i in range(1, len(nums)+1):
        j = 1
        roll = 0
        while True:
            cur = j * j * i
            if cur <= N:
                roll += nums[cur-1]
                j += 1
                answer = max(answer, roll)
            else:
                break
        
    return answer


nums = [8,7,3,5,7,2,4,9]
# nums = [8,10,3,8,1,13,7,9,4]

print(solution(nums))



def solution(nums):

    N = len(nums)
    ml = [1] * N
    ml[0] = nums[0]

    mr = [1] * N
    mr[-1] = nums[-1]


    for i in range(1, N):
        ml[i] = max(ml[i-1], nums[i])

    for i in range(N-2, -1, -1):
        mr[i] = max(mr[i+1], nums[i])

    answer = 0

    for i in range(1, N-1):
        answer = max(answer, (ml[i-1] -nums[i]) * mr[i+1])

    return answer


nums = [12,6,1,2,7]
nums = [1,10,3,4,19]
nums = [1,2,3]

print(solution(nums))

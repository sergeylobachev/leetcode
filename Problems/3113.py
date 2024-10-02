def solution(nums):
    l = len(nums)
    stack = []
    answer = 0
    for num in nums:
        while len(stack)> 0 and num > stack[-1][0]:
            e = stack.pop()
            answer += e[1] * (e[1] + 1) // 2 
        if len(stack) == 0:
            stack.append([num, 1])
        elif num == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([num, 1])

    while len(stack) > 0:
        e = stack.pop()
        answer += e[1] * (e[1] + 1) // 2

    return answer

nums = [3,3,3]

print(solution(nums))
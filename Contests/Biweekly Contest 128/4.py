from collections import Counter


def solution(nums):
    answer = []
    stack = []
    for i in range(len(nums)):
        cur = nums[i]
        popped = []
        while len(stack) > 0 and cur > stack[-1]:
            elem = stack.pop()
            popped.append(elem)

        stack.append(cur)

        cnt = Counter(popped)
        for value in cnt.values():
            answer.append(value)

    cnt = Counter(stack)
    for value in cnt.values():
        answer.append(value)
    
    total = 0
    for a in answer:
        total += a*(a+1) //2
    return total

nums = [1]
print(solution(nums))

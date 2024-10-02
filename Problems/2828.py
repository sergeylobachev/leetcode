def ps(n):
    ans = 0
    s = set()
    while n > 1:
        i = 2
        while i * i <= n:
            if n % i == 0:
                s.add(i)
                n = n // i
                break
            i += 1
        else:
            s.add(n)
            n = 1

    return len(s)

def solution(nums, k):
    MOD = 10 ** 9 + 7
    N = len(nums)
    scores = [ps(num) for num in nums]
    left = [0] * N
    right = [0] * N
    count = [0] * N

    stack = []
    for i, score in enumerate(scores):
        while len(stack) > 0 and stack[-1][1] < score:
            stack.pop()
        stack.append([i, score])
        if len(stack) == 1:
            left[i] = i
        else:
            left[i] = i - stack[-2][0] - 1

    stack = []
    for i, score in enumerate(reversed(scores)):
        while len(stack) > 0 and stack[-1][1] <= score:
            stack.pop()
        stack.append([i, score])
        if len(stack) == 1:
            right[~i] = i
        else:
            right[~i] = i - stack[-2][0] - 1

    count = [(left[i] * right[i] + left[i] + right[i] + 1) for i in range(N)]
    zipped = [[nums[i], count[i]] for i in range(N)]
    zipped.sort(reverse = True)

    ans = 1
    i = 0
    while k > 0:
        ans = (ans * zipped[i][0]) % MOD
        k -= 1
        zipped[i][1] -= 1
        if zipped[i][1] == 0:
            i += 1

    return ans
        



nums = [19,12,14,6,10,18]
k = 3

nums = [3289,2832,14858,22011]
k = 6
print([ps(num) for num in nums])
print(solution(nums, k))


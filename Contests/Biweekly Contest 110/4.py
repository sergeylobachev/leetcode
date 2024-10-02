def solution(a, b, x):
    N = len(a)
    bsum = sum(b)
    asum = sum(a)

    nums = [(a[i], b[i]) for i in range(N)]
    nums.sort()

    for i in range(N):
        

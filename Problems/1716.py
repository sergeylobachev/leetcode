def solution(n):
    sstair = 28 * (n // 7) + (n % 7 +1) * ( n % 7) // 2
    lstair = 7 * (n // 7 - 1) * (n // 7) // 2 + (n % 7) * (n // 7)
    return sstair + lstair

print(solution(4))
print(solution(10))
print(solution(20))
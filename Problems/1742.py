from collections import defaultdict

def solution(lowLimit, highLimit):
    d = defaultdict(int)
    for i in range(lowLimit, highLimit + 1):
        ds = 0
        n = i
        while n > 0:
            digit = n % 10
            ds += digit
            n = (n - digit) // 10

        d[ds] += 1

    return d

print(solution(1, 10))
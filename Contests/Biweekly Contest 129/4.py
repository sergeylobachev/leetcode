from collections import defaultdict

def solution(n):
    def digitsum(num):
        s = 0
        while num > 0:
            d = num % 10
            s += d
            num = (num - d) // 10

        return s

    d = defaultdict(int)
    for i in range(1, n+1):
        d[digitsum(i)] += 1

    print(d)


solution(13)
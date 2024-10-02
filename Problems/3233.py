from bisect import bisect_left
from bisect import bisect_right
from math import sqrt

def solution(l, r):
    def sieve(n):
        primes = []
        nums = [0, 0] + [1] * (n-2)

        i = 2
        while i * i < n:
            if nums[i]:
                for j in range(2*i, n, i):
                    nums[j] = 0
            i += 1
        
        for i in range(n):
            if nums[i] == 1:
                primes.append(i)

        return primes

    primes = sieve(int(sqrt(r)) * 2)

    count = r - l + 1
    lPos = bisect_left(primes, l)
    rPos = bisect_right(primes, r)

    special = rPos - lPos

    return count - special

print(solution(4, 16))

    
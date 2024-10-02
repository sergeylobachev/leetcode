from collections import defaultdict
import math

def divisiors(n):
    if n == 1: return [1]

    primes = []
    while n > 1:
        k = 2
        while k * k <= n:
            if n % k == 0:
                primes.append(k)
                n = n // k
                break
            else:
                k += 1

        else:
            primes.append(n)
            n = 1



    print(primes)


print(divisiors(21))


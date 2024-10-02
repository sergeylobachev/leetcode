def getDivisors(n):
    primes = []
    divisors = set()

    while n > 0:
        k = 2
        while k * k <= n:
            if n % k == 0:
                primes.append(k)
                n //= k
                break
            k += 1
        else:
            primes.append(n)
            n = 0

    l = len(primes)

    for mask in range(1, 2 ** l + 1):
        divisor = 1
        for j in range(l):
            idx = mask % 2
            mask = mask // 2
            if idx:
                divisor *= primes[j]
        divisors.add(divisor)

    return divisors


print(getDivisors(96034523451))
print(getDivisors(17341234123))
print(getDivisors(14123443344))
print(getDivisors(24123417674))
print(getDivisors(32345234523))
print(getDivisors(92345234523))

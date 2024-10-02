def primes(n):
    p = []
    nums = [0, 0] + [1] * (n-2)

    i = 2
    while i * i < n:
        if nums[i]:
            for j in range(2*i, n, i):
                nums[j] = 0
        i += 1
    
    for i in range(n):
        if nums[i] == 1:
            p.append(i)

    return p


print(primes(1))
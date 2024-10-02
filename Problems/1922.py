
def fastpower(x, n, mod):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return (fastpower((x*x) % mod, n//2, mod) % mod)
    else:
        return ((x % mod) * fastpower((x*x) % mod, (n-1) // 2, mod) % mod)




print(fastpower(3, 5, 10))
print(fastpower(2, 2, 10))
print(fastpower(1, 5, 10))
print(fastpower(3, 3, 10))

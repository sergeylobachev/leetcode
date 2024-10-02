def b(num, i):
    return (num & 1 << i) >> i

print(b(8, 1))
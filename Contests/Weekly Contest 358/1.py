def ld(n):
    s = [c for c in str(n)]
    s.sort()
    ld = int(s[-1])
    return ld

print(ld(170))
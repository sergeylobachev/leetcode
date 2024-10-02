def ok(a, b):
    if a == b:
        return True
    a = str(a)
    b = str(b)
    N = len(a)
    for i in range(N):
        for j in range(i+1, N):
            new_a = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
            k = 0
            while new_a[k] == "0":
                k += 1
            no_lz_a = new_a[k:]
            print(new_a, no_lz_a)
            if no_lz_a == b:
                return True
            
    return False

print(ok(1, 1))
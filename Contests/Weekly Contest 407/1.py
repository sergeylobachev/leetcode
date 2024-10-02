def changes(n, k):
    counter = 0
    for i in range(32):
        nbit = int((n & 1 << i) > 0)
        kbit = int((k & 1 << i) > 0)
        print(nbit, kbit)
        
        if kbit == 1 and nbit == 0:
            return -1
        if kbit == 0 and nbit == 1:
            counter += 1
            
    return counter

n = 13
k = 4
n = 21
k = 21

n = 14
k = 13
print(changes(n, k))
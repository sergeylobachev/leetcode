n = 5

time = 0
mvalue = n
while True:
    if n == 1:
        print(time, " ", mvalue)
        break
    if n % 2 == 0:
        n //= 2
        time += 1
        mvalue = max(mvalue, n)
    else:
        n = 3*n + 1
        time += 1
        mvalue = max(mvalue, n)
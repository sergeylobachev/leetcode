def solution(a, b, n):

    def myxor(num, xor):
        for i in range(50):

    xor = []

    for i in range(n-1, -1, -1):
        bita = a & 1 << i
        bitb = b & 1 << i
        if bita > 0: bita = 1
        if bitb > 0: bitb = 1

        xa = (1-bita)
        xb = (1-bitb)
        if xa != xb:
            xor1 = xor.append(xa)
            xor2 = xor.append(xb)
            a1 = 
            a2 = 
            b1 = 
            b2 =
            



        else:
            xor.append(xa)


    print(xora)
    print(xorb)
print(solution(6, 7, 5))
def solution(s):
    N = len(s)
    z = 0
    ## want to convert to 0
    z_ops = 0

    for i in range(N//2-1, -1, -1):
        # print(i)
        if (int(s[i]) + z_ops) % 2 == 1:
            z_ops += 1
            z += i + 1

    z_ops = 0
    for i in range(N//2, N):
        # print(i)
        if (int(s[i]) + z_ops) % 2 == 1:
            z_ops += 1
            z += N - i

    o = 0
    o_ops = 0

    for i in range(N//2-1, -1, -1):
        # print(i)
        if (int(s[i]) + o_ops) % 2 == 0:
            o_ops += 1
            o += i + 1
        # print(f"i={i}, o={o} o_ops={o_ops}")

    o_ops = 0
    for i in range(N//2, N):
        # print(i)
        if (int(s[i]) + o_ops) % 2 == 0:
            o_ops += 1
            o += N - i
    #     print(f"i={i}, o={o} o_ops={o_ops}")

    # print(f"z={z}, o={o}")
    return min(z, o)


s = "0011"
s = "010101"
print(solution(s))
def upper_bound(num):

    for i in range(32):
        if num & (1 << i) == 0:
            return num >> i // 2






print(upper_bound(13))
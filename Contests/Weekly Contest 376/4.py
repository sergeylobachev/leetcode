def equalindrom(n):
    if n < 10:
        return n
    strn = str(n)
    N = len(strn)
    candidates = []
    if N % 2 == 0:
        left = strn[0 : N // 2]
        lo = str(int(left) - 1)
        mi = str(int(left))
        up = str(int(left) + 1)
        lo = int(lo + lo[::-1])
        mi = int(mi + mi[::-1])
        up = int(up + up[::-1])
        if lo < 10 ** 9:
            candidates.append(lo)
        if mi < 10 ** 9:
            candidates.append(mi)
        if up < 10 ** 9:
            candidates.append(up)

        ans = lo
        mindiff = abs(lo - n)
        for c in candidates:
            if abs(c-n) <= mindiff:
                mindiff = abs(c-n)
                ans = c
        
        return ans

    else:
        left = strn[0 : N // 2 + 1]
        lo = str(int(left) - 1)
        mi = str(int(left))
        up = str(int(left) + 1)
        lo = int(lo + lo[0:len(lo)-1][::-1])
        mi = int(mi + mi[0:len(mi)-1][::-1])
        up = int(up + up[0:len(up)-1][::-1])
        if lo < 10 ** 9:
            candidates.append(lo)
        if mi < 10 ** 9:
            candidates.append(mi)
        if up < 10 ** 9:
            candidates.append(up)

        ans = lo
        mindiff = abs(lo - n)
        for c in candidates:
            if abs(c-n) <= mindiff:
                mindiff = abs(c-n)
                ans = c
        
        return ans



print(equalindrom(22))
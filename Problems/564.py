def solution(n):
    N = len(n)
    candidates = []

    ## case of 99, 999, 9999, ...
    if all([n[i] == "9" for i in range(N)]) and len(n) > 1:
        return str(int(n)+2)

    ## case of 10, 100, 1000, ...
    if all([n[i] == "0" for i in range(1, N)]) and n[0] == "1":
        return str(int(n)-1)

    ## case of 101, 1001, 10001, ...
    if all([n[i] == "0" for i in range(1, N-1)]) and N > 1 and n[0] == n[-1] == "1":
        return str(int(n)-2)


    if N % 2: ## odd length
        prefix = n[0:N//2+1]
        a = str(int(prefix)-1)
        b = str(int(prefix))
        c = str(int(prefix)+1)

        a = int(a + a[::-1][1:])
        b = int(b + b[::-1][1:])
        c = int(c + c[::-1][1:])

        if str(a) != n:
            candidates.append(a)
        if str(b) != n:
            candidates.append(b)
        if str(c) != n:
            candidates.append(c)

        ans = -1
        mindiff = float("inf")

        for c in candidates:
            if abs(c-int(n)) < mindiff:
                ans = c
                mindiff = abs(c-int(n))

        return str(ans)

    else: ## even length
        prefix = n[0:N//2]
        a = str(int(prefix)-1)
        b = str(int(prefix))
        c = str(int(prefix)+1)

        a = int(a + a[::-1])
        b = int(b + b[::-1])
        c = int(c + c[::-1])

        if str(a) != n:
            candidates.append(a)
        if str(b) != n:
            candidates.append(b)
        if str(c) != n:
            candidates.append(c)

        ans = -1
        mindiff = float("inf")

        for c in candidates:
            if abs(c-int(n)) < mindiff:
                ans = c
                mindiff = abs(c-int(n))

        return str(ans)


print(solution("1001"))


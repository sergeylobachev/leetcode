def solution(n):
    if n < 4:
        return 0

    MOD = 10 ** 9 + 7

    """
    A: count(l) == 0
    B: count(e) < 2
    C: count(t) == 0
    """

    a = pow(25, n, MOD)
    b = pow(25, n, MOD) + n * pow(25, n-1, MOD)
    c = pow(25, n, MOD)

    ab = pow(24, n, MOD) + n * pow(24, n-1, MOD)
    bc = pow(24, n, MOD) + n * pow(24, n-1, MOD)
    ca = pow(24, n, MOD)

    abc = pow(23, n, MOD) + n * pow(23, n-1, MOD)

    good = pow(26, n, MOD)
    bad = (a + b + c - (ab + bc + ca) + abc) % MOD

    return good - bad

print(solution(10))
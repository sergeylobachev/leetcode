from math import gcd

def solution(e):
    a = 0
    b = 1
    idx = 0
    N = len(e)

    def step(a, b, idx):
        if e[idx] in {"+", "-"}:
            sign = e[idx]
            idx += 1
        else:
            sign = "+"

        c = ""
        d = ""
        while e[idx] != "/":
            c += e[idx]
            idx += 1
        c = int(c)
        idx += 1
        while idx < N and (e[idx] != "+" and e[idx] != "-"):
            d += e[idx]
            idx += 1
        d = int(d)

        ## a/b + c/d = (ad + bc) / bd
        if sign == "+":
            a, b = a*d + b*c, b*d
        else:
            a, b = a*d - b*c, b*d

        a, b = a // gcd(a, b), b // gcd(a, b)
        print(f"a={a}, b={b}, c={c}, d={d}, sign={sign}, idx={idx}")

        return a, b, idx

    while idx < N:
        a, b, idx = step(a, b, idx)
        # print(f"a={a}, b={b}, idx={idx}")

    return f"{a}/{b}"





e = "-1/2+1/2+1/3"
e = "1/3-1/2"
e = "-1/2+1/2"
print(solution(e))
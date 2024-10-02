
def search(pattern, text):
    ans = []
    d = 256
    MOD = 10 ** 9 + 7
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d) % MOD

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % MOD
        t = (d*t + ord(text[i])) % MOD

    # Find the match
    for i in range(n-m+1):
        if p == t:
            ans.append(i)

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % MOD

            if t < 0:
                t = t + MOD

    return ans

s = "GEEKS FOR GEEKS"
p = "GEEK"

print(search(p,s))
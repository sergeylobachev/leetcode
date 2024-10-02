def solution(s, a, b, k):
    def search(pattern, text):
        ans = []
        d = 256
        q = 10 ** 9 + 9
        m = len(pattern)
        n = len(text)
        p = 0
        t = 0
        h = 1
        i = 0
        j = 0

        for i in range(m-1):
            h = (h*d) % q

        # Calculate hash value for pattern and text
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(text[i])) % q

        # Find the match
        for i in range(n-m+1):
            if p == t:
                ans.append(i)

            if i < n-m:
                t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

                if t < 0:
                    t = t+q

        return ans

    iInd = []
    jInd = []
    ans = []

    iInd = search(a, s)
    jInd = search(b, s)

    for a in iInd:
        for b in jInd:
            if abs(a - b) <= k:
                ans.append(a)
                break
    
    ans.sort()
    return ans


s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15

print(solution(s, a, b, k))
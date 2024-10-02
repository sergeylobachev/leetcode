def solution(s, k):
    N = len(s)
    roll = [0] * (N+1)
    vowels = set("aeiou")
    v = 0
    c = 0
    roll[0] = [0, 0]
    ans = 0

    for idx, letter in enumerate(s):
        if letter in vowels:
            v += 1
        else:
            c += 1
        roll[idx+1] = [v, c]


    for l in range(1, N+1):
        for r in range(l+1, N+1):
            v = roll[r][0] - roll[l-1][0]
            c = roll[r][1] - roll[l-1][1]
            if v == c and (v * c) % k == 0:
                ans += 1

    return ans





s = "baeyh"
k = 2

s = "abba"
k = 1

s = "bcdf"
k = 1

print(solution(s, k))
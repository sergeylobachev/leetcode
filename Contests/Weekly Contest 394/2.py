import string

def solution(word):
    a = 0
    L, U = string.ascii_lowercase, string.ascii_uppercase
    h = [[-1, - 1] for _ in range(26)]

    for i, c in enumerate(word):
        if c in L:
            print(c)
            h[ord(c) - ord("a")][0] = i
        if (c in U) and (h[i][1] < 0):
            print(f"{c} in U")
            h[ord(c) - ord("A")][1] = i

    for lo, up in h:
        print(lo, up)
        if lo > 0 and up > 0 and lo < up:
            a += 1

    return a


word = "aaAbcBC"
print(solution(word))




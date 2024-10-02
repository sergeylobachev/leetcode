s = "lol"
k = 0

def solution(s, k):
    t = ""
    for schar in s:
        d_to_a = min(abs(ord(schar) - ord("a")), abs(26 - ord(schar) + ord("a")))
        print(schar, d_to_a, k)
        if k >= d_to_a:
            t += "a"
            k -= d_to_a
        elif 0 < k < d_to_a:
            t += chr(ord(schar) - k)
            k = 0
        else:
            t += schar
    return t

print(solution(s, k))

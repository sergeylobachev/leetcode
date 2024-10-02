def solution(s):
    N = len(s)
    t = [0] * (2*N + 1)

    for i in range(2*N+1):
        if i % 2 == 0:
            t[i] = "|"
        else:
            t[i] = s[i//2]

    t = "".join(t)
    answer = 0
    for i in range(2*N + 1):
        l = i
        r = i
        while l >= 0 and r < 2*N + 1 and t[l] == t[r]:
            if t[l] != "|":
                answer += 1
            l -= 1
            r += 1

    return answer



s = "aaa"
print(solution(s))
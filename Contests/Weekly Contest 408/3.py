def solution(s):
    N = len(s)
    rs = [0 for _ in range(N+1)]
    roll = 0
    ans = 0

    for i in range(N):
        roll += int(s[i])
        rs[i+1] = roll

    for r in range(N):
        if s[r] == "1":
            ans += 1
            ones = 1
            zeros = 0





s = "00011"
print(solution(s))
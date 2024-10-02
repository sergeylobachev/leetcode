def solution(num, k):
    l = len(str(num))
    ans = 0
    for i in range(0, l-k+1):
        d = int(str(num)[i:i+k])
        if d > 0 and num % d == 0:
            ans += 1
        print(d)

    return ans


print(solution(30003, 3))
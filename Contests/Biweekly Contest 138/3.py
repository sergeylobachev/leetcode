def solution(n, k):

    ans = 0

    if n % 2 == 0:
        l = n // 2
        for i in range(10 ** (l-1), 10 ** l):
            s = str(i)
            num = int(s + s[::-1])
            if num % k == 0:
                ans += 1

    else:
        l = n // 2
        for i in range(10 ** (l-1), 10 ** l):
            s = str(i)
            for j in range(10):
                num = int(s + str(j) + s[::-1])
                print(num)
                if num % k == 0:
                    ans += 1

    return ans


print(solution(3, 5))



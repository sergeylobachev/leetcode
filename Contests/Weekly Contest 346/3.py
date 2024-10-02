from collections import defaultdict

def solution(n):
    def ok(s, x):
        s = str(s)
        N = len(s)
        dp = defaultdict(set)
        dp[0].add(0)
        for r in range(N):
            for l in range(r+1):
                for val in dp[l]:
                    dp[r+1].add(val + int(s[l:r+1]))
        print(dp)
        if x in dp[N]:
            return True
        else:
            return False

    ans = 0
    for i in range(1, n+1):
        if ok(i*i, i):
            print(f"i={i}")
            ans += i*i

    return ans


# n = 25
# def ok(s):
#     s = str(s)
#     N = len(s)
#     dp = defaultdict(set)
#     dp[0].add(0)
#     for r in range(N):
#         for l in range(r+1):
#             for val in dp[l]:
#                 dp[r+1].add(val + int(s[l:r+1]))
#     print(dp)
#     if n in dp[N]:
#         return True
#     else:
#         return False


# print(ok("1234"))
print(solution(10))
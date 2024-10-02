from collections import defaultdict

def solution(cookies, k): 
    def dp(idx, d):
        nonlocal
        if idx == len(cookies):
            return max(d.values())
        else:
            answer = 10 ** 9
            for i in range(k):
                d[i] += cookies[idx]
                answer = min(answer, dp(idx+1, d))
                d[i] -= cookies[idx]

            return answer

    d = defaultdict(int)
    return dp(0, d)


cookies = [8,15,10,20,8]
k = 2

cookies = [6,1,3,2,2,4,1,2]
k = 3

print(solution(cookies, k))
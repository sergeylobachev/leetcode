from collections import Counter
from math import ceil

def solution(balls):
    cnt = Counter(balls)
    a = list(cnt.values())
    a.sort()
    print(a)

    MN = min(a)
    ans = 10 ** 5
    for k in range(1, MN+1):
        sum = 0
        for c in a:
            if c % k > c // k:
                break
            else:
                sum += ceil(c / (k+1))
        else:
            ans = min(ans, sum)

    return ans


balls = [3,2,3,2,3]
balls = [10,10,10,3,1,1]
print(solution(balls))
from math import inf

def solution(nums, k):
    ret = inf
    d = [inf] * 32
    for j, x in enumerate(nums):
        for i in range(32):
            if not (x & 1 << i):
                d[i] = inf
            elif d[i] == inf:
                d[i] = j
        l = sorted(set(d))


        # cumulative AND of all previously encountered elements is 0
        if l[0] != 0:
            ret = min(ret, k)

        b = 0
        for q in l:
            if q != inf:
                for t in range(32):
                    if d[t] == q:
                        b |= 1 << t
            ret = min(ret, abs(k - b))
    return ret

x = 4
y = 5
print(2 | y)

# nums = [6]
# k = 2

# print(solution(nums, k))
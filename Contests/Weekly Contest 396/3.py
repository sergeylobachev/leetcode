from collections import Counter


def solution(s):
    N = len(s)
    cnt = Counter(s)
    minfreq = min(cnt.values())

    def ok(n):
        for val in cnt.values():
            if val % n != 0:
                return False
        return True

    # k is the number of intervals
    # l - is the len of a single interval
    for k in range(minfreq, 0, -1):
        if ok(k):
            l = N // k
            print(f"k={k}, l={l}")
            baseCnt = Counter(s[:l])
            start = 0
            end = l
            while end <= N:
                curCnt = Counter(s[start:end])
                print(baseCnt, curCnt)
                if baseCnt != curCnt:
                    break
                start += l
                end += l
            else:
                return l

    return N


s = "pqqppqpqpq"
s = "abba"
s = "cdef"
s = "aabb"
print(solution(s))

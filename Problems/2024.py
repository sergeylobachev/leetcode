from collections import defaultdict

def can(answerKey, n, k):

    l = 0
    r = n-1
    d = defaultdict(int)
    for i in range(n):
        d[answerKey[i]] += 1
    
    if min(d["F"], d["T"]) <= k:
        return True

    while r < len(answerKey) - 1:
        d[answerKey[l]] -= 1
        l += 1
        r += 1
        d[answerKey[r]] += 1
        if min(d["F"], d["T"]) <= k:
            return True


    return False

atest = btest = 1

atest += 1
print(atest, btest)
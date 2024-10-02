def solution(s, k):
    candidates = []
    N = len(s)
    
    for i in range(N):
        cur = i
        curstr = ""
        counter = 0
        while cur < N and counter < k:
            if s[cur] == "1":
                counter += 1
            curstr = curstr + s[cur]
            cur += 1
            if counter == k:
                candidates.append(curstr)
    
    if len(candidates) == 0:
        return ""

    candlen = [len(c) for c in candidates]
    print(min(candlen))

    newcandidates = [c for c in candidates if len(c) == min(candlen)]
    return min(newcandidates)



s = "100011001"
k = 3

s = "1011"
k = 2

s = "000"
k = 1
print(solution(s, k))
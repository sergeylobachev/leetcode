from collections import Counter

def solution(strs):
    ans = []

    for s in strs:
        cnt = Counter(s)
        f = 0
        for i in range(len(ans)):
            if cnt == Counter(ans[i][0]):
                ans[i].append(s)
                f = 1

        if f == 0:
            ans.append([s])

        print(s, ans)

    return ans

strs = ["eat","tea","tan","ate","nat","bat"]
print(solution(strs))

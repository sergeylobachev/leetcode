from collections import Counter

def solution(word):
    ans = 0
    cheat = [
            1,1,1,1,1,1,1,1,
            2,2,2,2,2,2,2,2,
            3,3,3,3,3,3,3,3,
            4,4
            ]
    cnt = Counter(word)

    vals = []
    for c in cnt.values():
        vals.append(c)

    vals.sort(reverse=True)

    for i, val in enumerate(vals):
        ans += val * cheat[i]

    return ans

word = "aabbccddeeffgghhiiiiii"
word = "xyzxyzxyzxyz"

print(solution(word))




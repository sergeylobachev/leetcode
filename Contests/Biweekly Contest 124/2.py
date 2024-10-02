from collections import Counter

s = "aabcbbca"
# s = "abcd"

def solution(s):
    cnt = Counter(s)
    mfreq = max(cnt.values())
    charset = set()

    answer = ""

    for char in cnt.keys():
        if cnt[char] == mfreq:
            charset.add(char)

    print(charset)

    for i in range(len(s)):
        if s[~i] in charset:
            answer = answer + s[~i]
            charset.remove(s[~i])
            print(answer)
        if len(charset) == 0:
            return answer[::-1] 

print(solution(s))
import string
from collections import defaultdict
from collections import Counter

def solution(s):
    lowercase_letters = list(string.ascii_lowercase)
    d = {}
    qm = 0
    for letter in lowercase_letters:
        d[letter] = (0, letter)

    for letter in s:
        if letter != "?":
            d[letter] = (d[letter][0] + 1, letter)
        else:
            qm += 1

    qmarks = [None] * qm
    ans = [None] * len(s)

    for i in range(qm):
        freq, char = min(d.values())
        qmarks[i] = char
        d[char] = (d[char][0] + 1, char)

    qmarks.sort()
    j = 0

    for i in range(len(ans)):
        if s[i] != "?":
            ans[i] = s[i]
        else:
            ans[i] = qmarks[j]
            j += 1

    return "".join(ans)

    
s = "a?a?"
# s = "???" 
# s = "abcdefghijklmnopqrstuvwxy??"

print(solution(s))


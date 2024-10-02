from collections import defaultdict


def solution(s):

    d = defaultdict(list)
    answer = [None] * len(s)

    for idx, letter in enumerate(s):
        if letter != "*":
            answer[idx] = letter
            d[ord(letter) - ord("a")].append(idx)
        else:
            answer[idx] = "*"
            for i in range(26):
                if len(d[i]) > 0:
                    remIdx = d[i].pop()
                    answer[remIdx] = "*"
                    break

    ret = []
    for a in answer:
        if a != "*":
            ret.append(a)

    return "" if len(ret) == 0 else "".join(ret)


s = "aaba*"
s = "abb**a*d"
s = "abc"
# s = "s*z*"

print(solution(s))





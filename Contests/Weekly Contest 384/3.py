from collections import defaultdict


def solution(words):
    d = defaultdict(int)
    lens = []
    for word in words:
        lens.append(len(word))
        for char in word:
            d[char] += 1

    twos = 0
    ones = 0
    for c in d:
        ones += d[c] % 2
        twos += 2 * (d[c] // 2)

    lens.sort()
    for i, l in enumerate(lens):
        if l % 2 == 1 and ones > 0:
            lens[i] -= 1
            ones -= 1

    ret = 0
    for i in range(len(lens)):
        if twos >= lens[i]:
            ret += 1
            twos -= lens[i]
        else: break


    return ret

# words = ["abbb","ba","aa"]
words = ["abc","ab"]
# words = ["cd","ef","a"]


print(solution(words))
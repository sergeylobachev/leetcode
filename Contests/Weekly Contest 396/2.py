from collections import defaultdict
from collections import Counter


def solution(word, k):

    def hash(s):
        MOD = 10 ** 9 + 7
        hash = 71
        for i, c in enumerate(s):
            hash = hash * 1993 + ord(c)
            hash = hash % MOD

        return hash

    hashes = []

    N = len(word)
    for i in range(N // k):
        print(word[i*k:(i+1)*k])
        hashes.append(hash(word[i*k:(i+1)*k]))

    cnt = Counter(hashes)
    answer = N // k - max(cnt.values())
    return answer


word = "leetcodeleet"
k = 4
word = "leetcoleet"
k = 2

print(solution(word, k))
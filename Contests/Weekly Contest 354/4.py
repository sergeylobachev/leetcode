def solution(word, forbidden):
    N = len(word)
    f = set(forbidden)
    ans = 0
    r = N

    for i in range(N-1, -1, -1):
        for k in range(1, 11):
            if i + k <= N:
                if word[i: i+k] in f:
                    ans = max(ans, r-i-1)
                    r = min(r, i + k - 1)
                    break

        print(f"i={i}, r={r}, ans={ans}")

    ans = max(ans, r)

    return ans




word = "leetcode"
forbidden = ["de","le","e"]

word = "aaaabaaacc"
forbidden = ["bcca","aaa","aabaa","baaac"]


print(solution(word, forbidden))
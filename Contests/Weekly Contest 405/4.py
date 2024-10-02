from math import inf

def solution(target, words, costs):

    trie = {}
    for i, word in enumerate(words):
        node = trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["$"] = min(node["$"], costs[i]) if "$" in node else costs[i]

    N = len(target)
    dp = [inf for _ in range(N+1)]
    dp[0] = 0

    for i, c in enumerate(target):
        node = trie
        for j in range(i, n):
            if target[j] not in node:
                break
            node = node[target[j]]
            if "$" in node:
                dp[j+1] = min(dp[j+1], dp[i] + node["#"])

    return dp[-1] if dp[-1] != inf else -1



    


target = "abcdef"
words = ["abdef","abc","d","def","ef"]
costs = [100,1,1,10,5]


print(solution(target, words, costs))
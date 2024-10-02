import string


def solution(beginWord, endWord, wordList):
    
    b = beginWord
    e = endWord
    words = wordList

    if e not in words:
        return 0

    words.append(b)
    N = len(words)

    d = {words[i]:i for i in range(N)}
    al = [set() for _ in range(N)]

    for idx, word in enumerate(words):
        for i in range(len(word)):
            for char in list(string.ascii_lowercase):
                search = word[:i] + char + word[i+1:]
                if search in d:
                    al[idx].add(d[search])
                    al[d[search]].add(idx)

    color = ["white"] * N
    distance = [0] * N
    q = []
    q.append(d[b])
    color[d[b]] = "gray"

    while q:
        cur = q.pop(0)
        for next in al[cur]:
            if color[next] == "white":
                q.append(next)
                color[next] = "gray"
                distance[next] = distance[cur] + 1
            color[cur] = "black"

    return distance[d[e]] + 1

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

print(solution(beginWord, endWord, wordList))
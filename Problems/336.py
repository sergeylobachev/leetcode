def solution(words):
    lookup = {}
    answer = set()

    for i, word in enumerate(words):
        lookup[word] = i


    for i, word in enumerate(words):
        L = len(word)
        for j in range(1, L+1):
            prefix = word[0:j][::-1]
            if prefix in lookup and word + prefix == (word + prefix)[::-1] and i != lookup[prefix]:
                answer.add((i, lookup[prefix]))

        for j in range(L):
            suffix = word[j::][::-1]
            if suffix in lookup and suffix + word == (suffix + word)[::-1] and i != lookup[suffix]:
                answer.add((lookup[suffix], i))
        

    return list(answer)





words = ["abcd","dcba","lls","s","sssll"]

print(solution(words))














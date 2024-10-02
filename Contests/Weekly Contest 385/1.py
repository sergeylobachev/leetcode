
def solution(words):
    l = len(words)
    answer = 0
    for i in range(l):
        for j in range(i+1, l):
            li = len(words[i])
            lj = len(words[j])
            if lj >= li and words[j][:li] == words[i] and words[j][lj-li:] == words[i]:
                answer += 1

    return answer

# words = ["a","aba","ababa","aa"]
words = ["pa","papa","ma","mama"]
# words = ["abab","ab"]


print(solution(words))


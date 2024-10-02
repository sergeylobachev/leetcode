from collections import defaultdict



def solution(word):
    visited = set()
    answer = 0
    for c in word:
        if 97 <= ord(c) <= 122:
            visited.add(c)

    for c in visited:
        if c.upper() in word:
            answer +=1



    print(visited)
    return answer


word = "abBCab"
print(solution(word))

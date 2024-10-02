from collections import defaultdict

def solution(word):

    ans = ""

    counter = 0
    start =""

    for c in word:
        if start == "":
            start = c
            counter += 1
            continue

        elif start != "":
            if c == start and counter < 9:
                counter += 1
            else:
                ans += str(counter) + start
                start = c
                counter = 1

    ans += str(counter) + start

    
    return ans

word = "aabcde"
word = "aaaaaaaaaaaaaabbccaaf"

print(solution(word))




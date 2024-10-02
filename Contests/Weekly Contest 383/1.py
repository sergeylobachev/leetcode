

def solution(word, k):
    N = len(word)
    start = k 
    a = 1
    while start < N:
        remainder = word[start:N]
        if word[:N-start] == remainder:
            return a
        else:
            a += 1
            start += k

    return a



# word = "abacaba"
# k = 3

# word = "abacaba"
# k = 4

word = "abcbabcd"
k = 2

print(solution(word, k))
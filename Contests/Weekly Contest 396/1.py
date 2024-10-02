import string
def solution(word):

    vowels = ['a', 'e', 'i', 'o', 'u']

    l = string.ascii_lowercase
    u = string.ascii_uppercase

    threechar = (len(word) >= 3)
    alphanumeric = word.isalnum()
    vowel = False
    consonant = False

    for c in word:
        if c in l or c in u:
            if c.lower() in vowels:
                vowel = True
            else:
                consonant = True

    return threechar and alphanumeric and vowel and consonant

# word = "234Adas"
# word = "ab3"
word = "a3$e"
print(solution(word))
    

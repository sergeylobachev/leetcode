# надо чтобы возвращался отсортированный список всех стартовых позиций

# Returns Z array for given string str[]
def getZarr(string, pattern):

    string = pattern + "$" + string
    n = len(string)
    p = len(pattern)
    a = []
    z = ["**"] * n
    l, r, k = 0, 0, 0

    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            if z[i] == p:
                a.append(i-len(pattern)-1)
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
                if z[i] == p:
                    a.append(i-len(pattern)-1)
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                if z[i] == p:
                    a.append(i-len(pattern)-1)
                r -= 1

    return a
    


word = "AABZAABZCAABZAABZA"
# w = [1,1,2,26,1,1,2,26,3,1,1,2,26,1,1,2,26,1]

print(getZarr(word, "AAB"))
# print(getZarr(w, [1,1,2]))
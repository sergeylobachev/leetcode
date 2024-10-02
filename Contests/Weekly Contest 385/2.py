def solution(arr1, arr2):
    s = set()
    for word in arr1:
        w = str(word)
        for i in range(1, len(w) + 1):
            s.add(w[:i])


    answer = 0
    for word in arr2:
        w = str(word)
        for i in range(1, len(w) + 1):
            if w[:i] in s:
                answer = max(answer, i)

    return answer

arr1 = [1,10,100]
arr2 = [1000]

# arr1 = [1,2,3]
# arr2 = [4,4,4]

# arr1 = [1,3]
# arr2 = [32,22]

# arr1 = [2161,7400,4662]
# arr2 = [7542,7483,8628,3345]

print(solution(arr1, arr2))






def solution(arr, k, threshold):
    l = 0
    r = k-1
    answer = 0

    s = sum(arr[:k])
    if s >= k * threshold:
        answer += 1

    for i in range(len(arr)-k):
        s -= arr[l]
        l += 1
        r += 1
        s += arr[r]
        if s >= k * threshold:
            answer += 1

    return answer


# arr = [2,2,2,2,5,5,5,8]
# k = 3
# threshold = 4


arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5

print(solution(arr, k , threshold))
def solution(n, k):

    arr = [1] * n
    MOD = 10 ** 9 + 7

    for i in range(k):
        for i in range(1, n):
            arr[i] += arr[i-1]


        print(arr)

    return arr[-1] % MOD

print(solution(5, 3))

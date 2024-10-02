def solution(code, k):
    N = len(code)
    a = [0] * N

    for i in range(N):
        cur = 0
        if k >= 0:
            for j in range(1, k+1):
                cur += code[(i+j) % N]
        else:
            for j in range(1, abs(k)+1):
                print(f"i  = {i}, j = {j}, (i-j) % (k + 1)= {(i-j) % (k + 1)}")
                cur += code[(i-j) % N]
        a[i] = cur

    return a


code = [5,7,1,4]
print(solution(code, 3))
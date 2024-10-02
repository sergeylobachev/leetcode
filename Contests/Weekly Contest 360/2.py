def solution(n , t):
    MOD = 10 ** 9 + 7
    left = t // 2
    
    
    if left >= n:
        ans = n * (n+1) // 2

    else:
        right = n - left
        leftsum = (left) * (left + 1) // 2
        rightsum = right * (t + t + right - 1) // 2
        ans = leftsum + rightsum

    return ans % MOD


n = 2
target = 3

n = 3
target = 3

n = 1
target = 1

print(solution(n , target))


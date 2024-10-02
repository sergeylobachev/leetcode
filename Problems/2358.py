        
def solution(n):   
        
    l = 1
    r = n

    while l <= r:
        m = (r + l) // 2
        if (m * (m+1)) // 2 <= n:
            l = m + 1
        else:
            r = m - 1

    return l

print(solution(70))
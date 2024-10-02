def solution(r, b):
    mx = max(r, b)
    mn = min(r, b)
        
    l = 0
    u = 0
    for i in range(1, 40):
        l += i
        l, u = min(l, u), max(l, u)
        if l > mn or u > mx:
            return i-1


print(solution(2, 4))
print(solution(2, 1))
print(solution(1, 1))
print(solution(10, 1))
print(solution(91, 100))
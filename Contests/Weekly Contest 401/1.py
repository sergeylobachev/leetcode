def solution(n, k):
    idx = 0
    dir = "right"
    for i in range(k):
        if dir == "right" and idx < n-1:
            idx += 1
        elif dir == "right" and idx == n-1:
            idx -= 1
            dir = "left"
        elif dir == "left" and idx > 0:
            idx -= 1
        elif dir == "left" and idx == 0:
            idx += 1
            dir = "right"

        print(i, dir, idx)
            
    return idx

print(solution(5, 6))
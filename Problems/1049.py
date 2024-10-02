def solution(stones):
    N = len(stones)
    sm = sum(stones)
    ans = 10**3

    for mask in range(2**N):
        cursum = 0
        for i in range(N):
            if (mask & 1 << i) > 0:
                cursum += stones[i]
        
        print(mask, cursum)

stones = [31,26,33,21,40]
print(solution(stones))
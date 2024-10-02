

def solution(n, k):
    if n == 1:
        return 0
    m = 2 ** (n-1)
    if k == m:
        return 1
    if k < m:
        return solution(n-1, k)
    if k > m:
        print(f"k > m, returning solution from {n-1}, {k-m}")
        return int(not solution(n-1, (2 ** n) - k + 1))
    
print(solution(3, 7))
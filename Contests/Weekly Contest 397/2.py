def solution(energy, k):
    N = len(energy)
    ans = float("-inf")

    for i in range(1, k+1):
        idx = N - i
        cursum = 0
        while idx >= 0:
            cursum += energy[idx]
            idx -= k
            ans = max(ans, cursum)

    return ans





energy = [5,2,-10,-5,1]
k = 3

energy = [-2,-3,-1]
k = 2

print(solution(energy, k))
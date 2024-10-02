
def solution(m, n, h, v):
    h.sort()
    v.sort()

    hi = len(h) - 1
    vi = len(v) - 1

    hm = 1
    vm = 1

    ans = 0
    
    while hi >= 0 and vi >= 0:
        if h[hi] >= v[vi]:
            ans += h[hi] * vm
            hm += 1
            hi -= 1
        else:
            ans += v[vi] * hm
            vm += 1
            vi -= 1

    while vi >= 0:
        ans += v[vi] * hm
        vi -= 1

    while hi >= 0:
        ans += h[hi] * vm
        hi -= 1
        
    return ans


    

m = 3
n = 2
h = [1,3]
v = [5]

m = 2
n = 2
h = [7]
v = [4]

print(solution(m, n, h, v))
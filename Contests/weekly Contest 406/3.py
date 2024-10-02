def solution(m, n, hc, vc):

    hc.sort(reverse = True)
    vc.sort(reverse = True)
    hm = 1
    vm = 1
    hi = 0
    vi = 0
    hsum = sum(hc)
    vsum = sum(vc)

    ans = 0

    while hi < len(hc) and vi < len(vc):
        if vc[vi] + vsum >= hc[hi]  + hsum:
            vsum -= vc[vi]
            ans += vm * vc[vi]
            vi += 1
            hm += 1
            
        else:
            hsum -= hc[hi]
            ans += hm * hc[hi]
            hi += 1
            vm += 1
            
    while hi < len(hc):
        ans += hm * hc[hi]
        hi += 1

    while vi < len(vc):
        ans += vm * vc[vi]
        vi += 1

    return ans


m = 3
n = 2
hc = [1,3]
vc = [5]

m = 2
n = 2
hc = [7]
vc = [4]


m = 7
n = 4
hc = [13,6,12,14,4,7]
vc = [14,15,11]

print(solution(m, n, hc, vc))
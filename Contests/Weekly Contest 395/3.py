def solution(n, x):
    def tobin(k):
        a = []
        while k > 0:
            d = k % 2
            a.append(d)
            k =  (k-d) // 2

        return a

    def todec(a):
        ret = 0
        for i in range(len(a)):
            ret = ret * 2 + a[i]
        return ret 

    ax = tobin(x)
    l = len(ax)
    an = tobin(n-1)
    px = 0
    pn = 0

    print(f"ax={ax}, an={an}")

    while pn < len(an):
        if px == l:
            ax.append(an[pn])
            pn += 1
        else:
            if ax[px] == 1:
                px += 1
            else:
                ax[px] = an[pn]
                px += 1
                pn += 1

    return todec(ax[::-1])


print(solution(3, 1))
print(solution(3, 4))
print(solution(2, 7))


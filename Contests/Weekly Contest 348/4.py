from functools import cache

## 

def calc(s, mn, mx):
    if s == "0":
        return 0
    N = len(s)

    @cache
    def less(pos, cursum):
        if pos > len(s) - 1:
            return 0
        if pos == len(s) - 1 and mn <= cursum <= mx:
            return 1

        ans = 0
        for i in range(10):
            ans += less(pos+1, cursum + i)
    
        return ans

    @cache
    def same(pos, cursum):
        if pos > len(s):
            return 0

        if pos == len(s):
            if mn <= cursum <= mx:
                return 1
            else:
                return 0

        ans = 0
        if pos == 0:
            for i in range(1, int(s[0]) + 1):
                ans += same(pos+1, cursum + i)

        if pos > 0:
            for i in range(int(s[pos]) + 1):
                ans += same(pos+1, cursum + i)

        return ans

    return less(0,0) + same(0, 0)



print(calc("4179205230", 8, 46))

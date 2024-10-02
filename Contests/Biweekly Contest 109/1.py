from functools import cache
def solution(n, x):

    powers = [0] + []
    i = 1

    while i ** x <= n:
        powers.append(i ** x)
        i += 1
    
    l = len(powers)

    @cache 
    def dp(idx, cursum):
        if cursum == n:
            return 1
        
        x = 0
        idx += 1
        while idx < l and powers[idx] + cursum <= n:
            x += dp(idx, cursum + powers[idx])
            idx += 1

        return x

    return dp(0, 0)


print(solution(9, 1))

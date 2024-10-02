def solution(zero, one, limit):

    MOD = 10 ** 9 + 7

    @cache
    def dp(zero, one, streak, last_is_zero):
        if zero == one == 0:
            return 1

        ret = 0
        if last_is_zero and zero > 0 and streak + 1 <= limit:
            ret += dp(zero-1, one, streak+1, True)
        
        if not last_is_zero and one > 0 and streak + 1 <= limit:
            ret += dp(zero, one-1, streak+1, False)

        if last_is_zero and one > 0:
            ret += dp(zero, one-1, 1, False)

        if not last_is_zero and zero > 0:
            ret += dp(zero-1, one, 1, True)

        return ret % MOD

    return dp(zero, one, 0, True)

        



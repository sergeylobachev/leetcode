def solution(nums):

    def isPal(n):
        strn = str(n)
        N = len(strn)
        for i in range(N//2):
            if strn[i] != strn[~i]:
                return False
        return True

    nums.sort()
    N = len(nums)

    if N % 2: ## odd len
        median = nums[N//2]
        if isPal(median):
            return sum([abs(num - median) for num in nums])
        l = median - 1
        r = median + 1
        lval = float("inf")
        rval = float("inf")

        while True:
            if isPal(l):
                lval = sum([abs(num - l) for num in nums])
                break
            l -= 1
        print(l, lval)
        while r < 10 ** 9:
            if isPal(r):
                rval = sum([abs(num - r) for num in nums])
                break
            r += 1

        return min(lval, rval)



nums = [22,33,22,33,22]
nums = [1,2,3,4,5]
nums = [10,12,13,14,15,6]
nums = [307,321,322,327]
# nums = [301,309,312,322]
nums = [109,113,115,122,128]
print(solution(nums))
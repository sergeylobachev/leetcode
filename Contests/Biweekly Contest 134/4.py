def solution(nums, k):

    lastzero = [-1] * 32
    kbin = [0] * 32

    ans = 0

    for i in range(32):
        if k & 1 << i > 0:
            kbin[i] = 1

    for idx, num in enumerate(nums):

        ## added num
        for i in range(32):
            if num & 1 << i == 0:
                lastzero[i] = idx

        mxzero1 = -1
        mxzero0 = 10**10

        for i in range(32):
            if kbin[i] == 1:
                mxzero1 = max(mxzero1, lastzero[i])
            elif kbin[i] == 0:
                mxzero0 = min(mxzero0, lastzero[i])

        ones = (idx - mxzero1)
        zeroes = (idx - mxzero0)

        if ones > zeroes:
            ans += ones - zeroes

    return ans

# nums = [1,1,1]
# k = 1

# nums = [1,1,2]
# k = 1

nums = [1,2,3]
k = 2

print(solution(nums, k))

from bisect import bisect_left
from collections import defaultdict

def solution(nums):

    def bit(num, i):
        return (num & 1 << i) >> i

    N = len(nums)
    nums.sort()
    ans = 0
    for i in range(N):
        gl = i
        gr = bisect_left(nums, 2*nums[i]+1, i)
        for j in range(20, -1, -1):
            if gl == gr - 1:
                break
            bj = bit(nums[i], j)
            bjl = bit(nums[gl], j)
            bjr = bit(nums[gr-1], j)
            if bjl == bjr:
                continue
            l, r = gl, gr
            while l < r - 1:
                m = (l + r) // 2
                if bit(nums[m], j) == bjl:
                    l = m
                else:
                    r = m

            if bj != bjl:
                gl, gr = gl, r
            else:
                gl, gr = r, gr
                
        ans = max(ans, nums[i] ^ nums[gl])

    return ans



nums = [1,2,3,4,5]
nums = [10,100]
nums = [500,520,2500,3000]
print(solution(nums))




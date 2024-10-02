from sortedcontainers import SortedList
from bisect import bisect_left
from bisect import bisect_right

def solution(nums):
    N = len(nums)
    sl = SortedList()
    ls = []
    lb = []
    rs = []
    rb = []

    for i in range(N-1, -1, -1):
        posBigger = sl.bisect_right(nums[i])
        posSmaller = sl.bisect_left(nums[i])
        rb.append(len(sl) - posBigger)
        rs.append(posSmaller)
        sl.add(nums[i])

    rs = rs[::-1]
    rb = rb[::-1]

    sl = SortedList()
    for i in range(N):
        posBigger = sl.bisect_right(nums[i])
        posSmaller = sl.bisect_left(nums[i])
        lb.append(len(sl) - posBigger)
        ls.append(posSmaller)
        sl.add(nums[i])

    ans = 0
    for i in range(N):
        ans += ls[i] * rb[i] + lb[i] * rs[i]

    return ans


nums = [2,5,3,4,1]

print(solution(nums))
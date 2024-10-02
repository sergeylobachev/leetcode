from collections import Counter
from collections import defaultdict
from math import inf

def solution(nums, k):
    N = len(nums)

    diffs = defaultdict(int)
    limits = defaultdict(int)

    for i in range(N // 2):
        a = min(nums[i], nums[~i])
        b = max(nums[i], nums[~i])
        diffs[b-a] += 1
        limits[max(k-a, b)] += 1

    print(diffs)
    print(limits)
    ## Total cost = N + count2 - count0

    ans = inf
    twos = 0
    for x in range(k+1):
        curcost = N // 2 + twos - diffs[x]
        ans = min(ans, curcost)
        twos += limits[x]

    return ans


nums = [0,1,2,3,3,6,5,4]
k = 6

# nums = [1,0,1,2,4,3]
# k = 4

print(solution(nums, k))
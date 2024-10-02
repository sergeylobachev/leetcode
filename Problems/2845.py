from collections import defaultdict

def solution(nums, modulo, k):
    d = defaultdict(int)
    d[0] = 1
    N = len(nums)
    roll = 0
    ans = 0
    for i in range(N):
        if nums[i] % modulo == k:
            roll += 1
        ans += d[(roll - k) % modulo]
        d[roll % modulo] += 1

    print(d)
    return ans


nums = [3,2,4]
modulo = 2
k = 1

# nums = [3,1,9,6]
# modulo = 3
# k = 0

print(solution(nums, modulo, k))







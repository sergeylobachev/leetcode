def solution(nums, k):

    n = [0] * 32
    nk = [0] * 32
    N = len(nums)

    for num in nums:
        for i in range(32):
            if (num & 1 << i) > 0:
                n[i] += 1

    for j in range(32):
        if n[j] % 2:
            n[j] = 1
        else:
            n[j] = 0

    for i in range(32):
        if (k & 1 << i) > 0:
            nk[i] = 1

    ans = 0

    for j in range(32):
        if n[j] != nk[j]:
            ans += 1

    return ans


nums = [2,1,3,4]
k = 1

# nums = [2,0,2,0]
# k = 0

print(solution(nums, k))
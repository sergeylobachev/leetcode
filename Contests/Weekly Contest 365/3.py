from collections import defaultdict

def solution(nums, target):
    s = sum(nums)
    N = len(nums)

    k = target // s
    target %= s

    if target == 0:
        return k*N

    A = nums + nums
    l = 0
    w = 0
    ans = 10 ** 10
    for i in range(A):
        w += A[i]
        while w >= target:
            if w == target:
                ans = min(ans, i-l+1)
            w -= A[l]
            l += 1
  
    if ans == 10 ** 10:
        return -1
    else:
        return ans + N * k



nums = [2,4,6,8]
target = 3
nums = [1,2,3,3]
target = 8
nums = [1,1,1,2,3]
target = 4

nums = [1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6]
target = 56

print(solution(nums, target))
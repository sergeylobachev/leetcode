def solution(nums):
    N = len(nums)
    l = 0
    r = N-1
    p = N-1
    print(p)
    ans = [0] * N

    while l < r:
        if nums[l] ** 2 > nums[r] ** 2:
            ans[p] = nums[l] ** 2
            l += 1
        else:
            ans[p] = nums[r] ** 2
            r -= 1
        p -= 1
        print(ans)

    return ans

nums = [-4,-1,0,3,10]
print(solution(nums))
from collections import defaultdict

def solution(nums, k):
    N = len(nums)
    psum = [0] * N
    psum[0] = nums[0]
    for i in range(1, N):
        psum[i] = psum[i-1] + nums[i]
    print(psum)
    ans = float("-inf")
    d = defaultdict()


    for i, num in enumerate(nums):
        if num-k in d:
            ans = max(ans, psum[i] - psum[d[num-k]] + nums[d[num-k]])
        if num+k in d:
            ans = max(ans, psum[i] - psum[d[num+k]] + nums[d[num+k]])
        
        if (num not in d) or psum[i] <= psum[d[num]]:
            d[num] = i

        print(i, d, ans)

    if ans == float("-inf"):
        return 0
    else:
        return ans




nums = [3,3]
k = 2
print(solution(nums, k))
    

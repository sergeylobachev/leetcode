

def solution(nums, queries):
    N = len(nums)
    msum = [0] * N
    ans = [True] * len(queries)
    cur = 0
    for i in range(1, N):
        if (nums[i] - nums[i-1]) % 2 == 0:
            cur += 1
        msum[i] = cur

    for i, q in enumerate(queries):
        ans[i] = msum[q[0]] == msum[q[1]]
            
    return ans

nums = [3,4,1,2,6]
queries = [[0,4]]

# nums = [4,3,1,6]
# queries = [[0,2],[2,3]]

print(solution(nums, queries))


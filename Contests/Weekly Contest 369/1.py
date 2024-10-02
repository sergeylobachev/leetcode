def solution(nums, k):
    ans = [0] * 32

    for num in nums:
        for i in range(32):
            if (num & 1 << i) > 0:
                ans[i] += 1


    answer = 0
    for i in range(32):
        if ans[i] >= k:
            answer += 2 ** i

    return answer



nums = [7,12,9,8,9,15]
k = 4 

nums = [2,12,1,11,4,5]
k = 6

nums = [10,8,5,9,11,6,8]
k = 1 

print(solution(nums, k))
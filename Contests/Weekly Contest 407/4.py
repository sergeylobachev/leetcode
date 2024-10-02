def solution(nums, target):
    N = len(nums)
    k = [nums[i]-target[i] for i in range(N)]

    print(k)

    # ans = abs(k[0])
    # for i in range(1, N):
    #     if k[i] * k[i-1] <= 0:
    #         ans += abs(k[i])
    #     else:
    #         ans += abs(abs(k[i]) - abs(k[i-1]))

    # return ans



    

nums = [3,5,1,2]
target = [4,6,2,4]

nums = [1,3,2]
target = [2,1,4]

nums = [9,2,6,10,4,8,3,4,2,3]
target = [9,5,5,1,7,9,8,7,6,5]

print(solution(nums, target))
from collections import Counter

def solution(nums, limit):
    N = len(nums)
    ans = [] * N
    cnt = Counter(nums)
    cnt = list(sorted(cnt.items()))
    print(cnt)
    # for num in nums:
    #     target = num - k
    #     l = 0
    #     r = len(cnt)
    #     while True:
    #         m = l + r // 2
    #         if counter[]





nums = [1,5,3,9,8]
limit = 2

print(solution(nums, limit))
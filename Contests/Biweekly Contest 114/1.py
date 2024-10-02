def solution(nums, k):
    s = set(i for i in range(1, k+1))
    ns = set()
    counter = 0
    n = len(nums)
    for i in range(n-1, -1, -1):
        counter += 1
        if nums[i] <= k:
            ns.add(nums[i])
            
        print(counter, ns)
        if len(s) == len(ns):
            return counter


nums = [1, 2, 2]
k = 2

print(solution(nums, k))
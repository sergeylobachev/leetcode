def solution(nums, pattern):
    N = len(nums)
    P = len(pattern)
    psum = sum(pattern)

    for i in range(1, N):
        if nums[i] > nums[i-1]:
            nums[i-1] = 1
        elif nums[i] == nums[i-1]:
            nums[i-1] = 0
        else:
            nums[i-1] = - 1

    del nums[-1]
    ret = 0

    s = sum(nums[:P+1])
    for i in range(N-P):
        





nums = [1,4,4,1,3,5,5,3]
pattern = [1,0,-1]
solution(nums, pattern)
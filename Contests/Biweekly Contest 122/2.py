def solution(nums):
    def bits(n):
        ans = 0
        for i in range(32):
            if n & 1 << i > 0:
                ans += 1
        return ans
    
    N = len(nums)
    for num in nums:
        print(num, bits(num))
        
    for i in range(N):
        for j in range(i+1, N):
            if nums[i] > nums[j] and bits(nums[i]) != bits(nums[j]):
                return False
            
    return True

nums = [8,4,2,30,15]

print(solution(nums))
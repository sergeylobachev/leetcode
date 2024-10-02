def solution(nums, k):
    def cbits(n):
        ret = 0
        for i in range(32):
            if (n & 1 << i) > 0:
                ret += 1
                
        return ret
                    
    answer = 0
    for num in nums:
        print(num, cbits(num))
            
    return answer


nums = [5,10,1,5,2]
k = 1
print(solution(nums, k))
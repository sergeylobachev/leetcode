def solution(nums, k):
    ans = 0
    for num in nums:
        a = num 
        counter = 0
        while num:
            print(num)
            counter += num & 1
            num >>= 1


        if counter == k:
            print("a=", a)
            ans += a

    return ans


nums = [5,10,1,5,2]
k = 1
print(solution(nums, k))

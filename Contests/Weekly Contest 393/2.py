def solution(nums):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    p = set(primes)
    
    left = -1
    right = -1
    
    for i in range(len(nums)):
        if nums[i] in p:
            left = i
            break
            
    for i in range(len(nums)-1, -1, -1):
        if nums[i] in p:
            right = i
            break

    print(left)
    print(right)
    return right-left


nums = [4,8,2,8]

print(solution(nums))
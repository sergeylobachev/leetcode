

def solution(nums):
    N = len(nums)
    ans = 1
    ones = 0
    cur_int = 0
    
    for i in range(N):
        if nums[i] == 1:
            ones += 1
            if 2 <= ones:
                ans *= (cur_int + 1)
            cur_int = 0

        if nums[i] == 0:
            cur_int += 1

        print(f"i={i}, ones={ones}, cur_int={cur_int}, ans={ans}")
                
    return ans

nums = [1,0,0,0,1,0,0,1,0,0]

print(solution(nums))
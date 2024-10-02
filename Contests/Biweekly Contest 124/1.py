def solution(nums):
    answer = 1
    number = nums[0] + nums[1]
    i = 2
    while i + 1 <= len(nums) - 1:
        if number == nums[i] + nums[i+1]:
            answer += 1
            i += 2
        else:
            break

    return answer
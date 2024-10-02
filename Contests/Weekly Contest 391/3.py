nums = [0,1,1,1]


def solution(nums):
    answer = 0
    lens = []
    curnumber = nums[0]
    curlen = 1
    pointer = 0
    while pointer < len(nums):
        if pointer + 1 == len(nums):
            lens.append(curlen)
            pointer += 1
        elif nums[pointer + 1] != nums[pointer]:
            curlen += 1
            pointer += 1
        else:
            lens.append(curlen)
            curlen = 1
            pointer += 1
    
    for l in lens:
        answer += l * (l+1) // 2
    
    return answer

print(solution(nums))
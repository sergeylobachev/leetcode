nums = [0]

def solution(l, nums, advantage):
    if l == "a":
        if len(nums) == 0 and advantage >= 0:
            return True
        elif len(nums) == 0 and advantage < 0:
            return False
        else:
            return not solution("b", nums[1:], (advantage + nums[0]) * -1) or not solution("b", nums[:-1], (advantage + nums[-1]) * -1)
    if l == "b":
        if len(nums) == 0 and advantage > 0:
            return True
        elif len(nums) == 0 and advantage <= 0:
            return False
        else:
            return not solution("a", nums[1:], (advantage + nums[0]) * -1) or not solution("a", nums[:-1], (advantage + nums[-1]) * -1)


print(solution("a", nums, 0))

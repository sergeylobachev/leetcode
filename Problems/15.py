from collections import defaultdict


def solution(nums):

    ans = set()
    nums.sort()

    def helper(l, r, t):
        while l < r:
            s = nums[l] + nums[r]
            if s == t:
                ans.add((-t, nums[l], nums[r]))
            if s < t:
                l += 1
            else:
                r -= 1

    i = 0
    cur = float("inf")

    while i < len(nums)-2:
        if nums[i] == cur:
            i += 1
        else:
            print(nums[i])
            cur = nums[i]
            helper(i+1, len(nums)-1, -nums[i])
            i += 1

    return list(ans)


    
# nums = [1, 2, 3, 3, 3, 5, 6, 6]
# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]
# nums = [0, 0, 0, 0]
nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
# [-82, -70, -66, -49, -43, -29, -29, -14, -11, -6, -3, -3, 1, 2, 10, 12, 13, 15, 15, 17, 21, 26, 26, 28, 28, 29, 31, 33, 34, 36, 43, 46, 46, 47, 48, 49, 52, 55, 55, 56, 57, 61, 62, 65, 69, 71, 74, 76, 77, 79, 83, 84, 86, 93, 94]

print(solution(nums))
















# ans = set()
# nums.sort()

# def helper(l, r, t):
#     while l < r:
#         s = nums[l] + nums[r]
#         if s == t:
#             ans.add((-t, nums[l], nums[r]))
#         if s < t:
#             l += 1
#         else:
#             r -= 1

#     return ans

# print(helper(8, len(nums)-1, 14))


# difference = {(-14, 2, 12), (-14, -3, 17), (-11, -6, 17), (-3, 1, 2), (-14, 1, 13), (-11, 1, 10)}




# a = [[-49,21,28],[-70,34,36],[-49,-3,52],[-82,34,48],[-70,-6,76],[-82,26,56],[-70,1,69],[-43,15,28],[-70,-14,84],[-82,33,49],[-29,-14,43],[-66,10,56],[-29,1,28],[-82,17,65],[-66,1,65],[-66,17,49],[-49,-6,55],[-43,-3,46],[-49,1,48],[-49,2,47],[-70,15,55],[-43,12,31],[-70,13,57],[-82,13,69],[-49,15,34],[-82,21,61],[-82,36,46],[-82,-11,93],[-70,21,49],[-43,-6,49],[-43,10,33],[-66,-11,77],[-49,13,36],[-29,12,17],[-43,17,26],[-43,-14,57],[-66,-3,69]]
# b = [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]

# c = set(map(lambda x: tuple(x), a))
# d = set(map(lambda x: tuple(x), b))
# print(len(a), len(c), len(b), len(d))

# print(c.difference(d))
# print(d.difference(c))

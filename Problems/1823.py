

def solution(n, k):
    friends = [i for i in range(n)]
    i_start = 0
    while len(friends) > 1:
        i_leaves = (i_leaves + k - 1) % len(friends)
        if i_leaves == len(friends) - 1:
            i_start = 0
        else:
            i_start = i_leaves
            
        del friends[i_leaves]
    return friends[0] + 1

def winner(n, k):
    nums = list(range(n))
    i = 0 
    while len(nums) > 1: 
        i = (i + k-1) % len(nums)
        nums.pop(i)
    return nums[0] + 1


print(solution(5, 2))
print(winner(5, 2))
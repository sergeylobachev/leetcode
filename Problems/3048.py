# Test case 1
# nums = [2,2,0]
# changeIndices = [2,2,2,2,3,2,2,1]

# Test case 2
# nums = [1,3]
# changeIndices = [1,1,1,2,1,1,1]


# Test case 3
# nums = [0,1]
# changeIndices = [2,2,2]



def valid(start, nums, changeIndices):
    unmarked = set([i+1 for i in range(len(nums))])

    counter = 0
    for i in range(start, -1, -1):
        if changeIndices[i] in unmarked:
            counter += nums[changeIndices[i]-1]
            unmarked.remove(changeIndices[i])
        else:
            if counter > 0: counter -= 1

        print(f"step {i}, counter  is {counter}", unmarked)

    if len(unmarked) > 0: return False
    return counter <= 0

def bs(nums, changeIndices):
    left = 0 
    right = len(changeIndices) - 1
    if valid(right, nums, changeIndices) == 0:
        return -1
    
    while left <= right:
        mid = left + (right-left) // 2
        if valid(mid, nums, changeIndices):
            right = mid - 1
        else:
            left = mid + 1

    return left + 1



# Test case 1
# nums = [2,2,0]
# changeIndices = [2,2,2,2,3,2,2,1]

# Test case 2
# nums = [1,3]
# changeIndices = [1,1,1,2,1,1,1]


# Test case 3
# nums = [0,1]
# changeIndices = [2,2,2]



print(bs(nums, changeIndices))


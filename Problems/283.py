nums = [0]

def movezeros(nums):
    zero_counter = 0
    cur_index = 0

    for num in nums:
        if num == 0:
            zero_counter += 1
        else:
            nums[cur_index] = num
            cur_index += 1

    for i in range(0, zero_counter):
        nums[~i] = 0

    print(nums)


movezeros(nums)
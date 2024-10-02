def quicksort(nums, l, r):

    def partition(nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i + 1

    if l < r:
        p = partition(nums, l, r)
        quicksort(nums, l, p-1)
        quicksort(nums, p+1, r)






nums = [7, 4, 14, 11, 2, 2, 1, 9]

# def partition(nums, l, r):
#     pivot = nums[r]
#     i = l - 1
#     for j in range(l, r):
#         if nums[j] <= pivot:
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#         print("j=", j, nums)
#     nums[i+1], nums[r] = nums[r], nums[i+1]
#     return i + 1

# print(partition(nums, 0, len(nums)-1))
# print(nums)
quicksort(nums, 0, len(nums)-1)
print(nums)


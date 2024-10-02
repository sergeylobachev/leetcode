nums1 = [4,1,2]
nums2 = [1,3,4,2]


def solution(nums1, nums2):
    ans = [0] * len(nums1)

    for i in range(len(nums1)):
        j = 0
        while nums1[i] != nums2[j]:
            j += 1

        print(f"i = {i}, j = {j}")
        while j < len(nums2) and nums2[j] <= nums1[i]:
            j += 1
        print(f"i = {i}, j = {j}")
        ans[i] = nums2[j] if j < len(nums2) else -1

    return ans


print(solution(nums1, nums2))
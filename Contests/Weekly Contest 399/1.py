
def solution(nums1, nums2, k):

    ans = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                ans += 1

    return ans


nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1

print(solution(nums1, nums2, k))
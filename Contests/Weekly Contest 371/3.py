def solution(nums1, nums2):

    N = len(nums1)
    lmin = min(nums1[-1], nums2[-1])
    lmax = max(nums1[-1], nums2[-1])
    a, b, c, d = 0, 0, 0, 0

    for i in range(N):
        if min(nums1[i], nums2[i]) > lmin:
            return -1
        if max(nums1[i], nums2[i]) > lmax:
            return -1
        if nums1[i] > lmin:
            a += 1
        if nums2[i] > lmin:
            b += 1
        
    return min(a, b)

nums1 = [1,2,7]
nums2 = [4,5,3]


# nums1 = [1,5,4]
# nums2 = [2,5,3]

print(solution(nums1, nums2))
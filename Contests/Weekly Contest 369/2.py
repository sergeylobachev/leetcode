from collections import Counter

def solution(nums1, nums2):
    cnt1 = Counter(nums1)
    cnt2 = Counter(nums2)
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    z1 = cnt1[0]
    z2 = cnt2[0]

    if z1 == 0 and sum1 < sum2 + z2:
        return -1
    if z2 == 0 and sum2 < sum1 + z1:
        return -1
    
    return max(sum1 + z1, sum2 + z2)


nums1 = [3,2,0,1,0]
nums2 = [6,5,0]

nums1 = [2,0,2,0]
nums2 = [1,4]

print(solution(nums1, nums2))
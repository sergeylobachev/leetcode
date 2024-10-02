from collections import defaultdict
from collections import Counter


def solution(nums1, nums2, k):
    ans = 0
    dict1 = Counter(nums1)
    dict2 = Counter([k*num for num in nums2])

    for d1 in dict1:
        for i in range(1, int(d1 ** 0.5) + 1):
            if d1 % i == 0:
                factor = i
                cofactor = d1 // i

                if factor in dict2:
                    ans += dict1[d1] * dict2[factor]
                if cofactor in dict2 and cofactor != factor:
                    ans += dict1[d1] * dict2[cofactor]

    return ans


nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1


# nums1 = [7]
# nums2 = [7]
# k = 1

print(solution(nums1, nums2, k))
    
    
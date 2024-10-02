

def solution(nums1, nums2):

    N = len(nums1)

    nums1.sort()
    nums2.sort()

    def isok(nums1, nums2):
        N = len(nums1)
        for i in range(N-1):
            if nums1[i] - nums2[i] != nums1[i+1] - nums2[i+1]:
                return False
        
        return True


    for i in range(0, N-1):
        for j in range(i+1, N):
            n = nums1[:i] + nums1[i+1:j] + nums1[j+1:]
            if isok(n, nums2):
                return nums2[0] - n[0]

    

# nums1 = [4,20,16,12,8]
# nums2 = [14,18,10]

nums1 = [3,5,5,3]
nums2 = [7,7]

print(solution(nums1, nums2))
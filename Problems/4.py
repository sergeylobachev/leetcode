def solution(nums1, nums2):

    A = nums1
    B = nums2

    if len(B) < len(A):
        A, B = B, A

    la = len(A)
    lb = len(B)

    half = (len(A) + len(B)) // 2

    l = 0
    r = la - 1

    while True:
        m = (l + r ) // 2
        j = half - m - 2

        Aleft = A[m] if m >= 0 else float("-inf")
        Aright = A[m+1] if (m+1) < la else float("inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Bright = B[j+1] if (j+1) < lb else float("inf")

        if Aleft <= Bright and Bleft <= Aright:
            if (len(A) + len(B)) % 2 != 0:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        elif Aleft > Bright:
            r = m - 1
        else:
            l = m + 1

        
nums1 = [1,2]
nums2 = [3,4]    

print(solution(nums1, nums2))



    





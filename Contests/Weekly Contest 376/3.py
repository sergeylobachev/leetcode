def solution(nums):
    def equalindrom(n):
        strn = str(n)
        N = len(strn)
        candidates = []
        if N % 2 == 0:
            left = strn[0 : N // 2]
            lo = str(int(left) - 1)
            mi = str(int(left))
            up = str(int(left) + 1)
            lo = int(lo + lo[::-1])
            mi = int(mi + mi[::-1])
            up = int(up + up[::-1])
            if lo < 10 ** 9:
                candidates.append(lo)
            if mi < 10 ** 9:
                candidates.append(mi)
            if up < 10 ** 9:
                candidates.append(up)

            ans = lo
            mindiff = abs(lo - n)
            for c in candidates:
                if abs(c-n) <= mindiff:
                    mindiff = abs(c-n)
                    ans = c
            
            return ans

        else:
            left = strn[0 : N // 2 + 1]
            lo = str(int(left) - 1)
            mi = str(int(left))
            up = str(int(left) + 1)
            lo = int(lo + lo[0:len(lo)-1][::-1])
            mi = int(mi + mi[0:len(mi)-1][::-1])
            up = int(up + up[0:len(up)-1][::-1])
            if lo < 10 ** 9:
                candidates.append(lo)
            if mi < 10 ** 9:
                candidates.append(mi)
            if up < 10 ** 9:
                candidates.append(up)

            ans = lo
            mindiff = abs(lo - n)
            for c in candidates:
                if abs(c-n) <= mindiff:
                    mindiff = abs(c-n)
                    ans = c
            
            return ans


    N = len(nums)
    if N % 2 == 0:
        option1 = equalindrom(nums[N//2])
        option2 = equalindrom(nums[N//2] + 1)
        ans1 = sum([abs(num-option1) for num in nums])
        ans2 = sum([abs(num-option2) for num in nums])

        return min(ans1, ans2)
    
    else:
        option1 = equalindrom(nums[N//2])
        option2 = equalindrom(nums[N//2])
        ans1 = sum([abs(num-option1) for num in nums])
        ans2 = sum([abs(num-option2) for num in nums])

        return min(ans1, ans2)



    




nums = [1,2,3,4,5]
nums = [10,12,13,14,15]
print(solution(nums))
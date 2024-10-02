nums = [52, 98]
k = 82


def solution(nums, k):
    l = len(nums)
    nums.sort()
    answer = 0

    if l % 2 == 1:
        if nums[l//2] == k:
            return 0
        elif nums[l//2] > k:
            i = 0
            while i <= l // 2:
                answer += max(nums[i] - k, 0)
                i += 1
            return answer
        else:
            i = l // 2
            while i < l:
                answer += max(k-nums[i], 0)
                i += 1
            return answer
    
    if l % 2 == 0:
        answer = 0
        i = 0
        while i <= l // 2:
            if nums[i] > k:
                answer += nums[i] - k
            i += 1

        i = l // 2
        while i < l:
            if nums[i] < k:
                answer += k -nums[i]
            i += 1

        return answer



        
print(solution(nums, k))


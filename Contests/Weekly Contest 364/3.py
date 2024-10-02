def solution(nums):
    N = len(nums)
    l = [0] * N 
    r = [0] * N

    s = []
    cursum = 0
    for i, num in enumerate(nums):
        counter = 1
        while len(s) > 0 and num <= s[-1][0]:
            popped_val, popped_count = s.pop()
            cursum -= (popped_val - num) * popped_count
            counter += popped_count

        cursum += num
        s.append((num, counter))
        l[i] = cursum

    s = []
    cursum = 0
    for i, num in enumerate(nums[::-1]):
        counter = 1
        while len(s) > 0 and num <= s[-1][0]:
            popped_val, popped_count = s.pop()
            cursum -= (popped_val - num) * popped_count
            counter += popped_count

        cursum += num
        s.append((num, counter))
        r[i] = cursum

    r = r[::-1]

    ans = 0
    for i in range(N):
        ans = max(ans, l[i]+r[i]-nums[i])

    return ans


maxHeights = [5,3,4,1,1]
maxHeights = [6,5,3,9,2,7]
maxHeights = [3,2,5,5,2,3]

print(solution(maxHeights))
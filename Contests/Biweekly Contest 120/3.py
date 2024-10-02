from bisect import bisect_left
from bisect import bisect_right

def solution(nums):
    N = len(nums)

    left = [nums[0]]
    l = 0

    right = [nums[-1]]
    r = N-1

    ans = 0

    for i in range(1, N):
        if nums[i] > left[-1]:
            left.append(nums[i])
            l += 1
        else:
             break

    for i in range(N-2, -1, -1):
        if nums[i] < right[-1]:
            right.append(nums[i])
            r -= 1
        else:
            break
    right = right[::-1]

    print(left, l)
    print(right, r)

    if l >= r:
        return N * (N+1) // 2

    for i, lnum in enumerate(left):
        rpos = bisect_right(right, lnum)
        ans += len(right) - rpos + 1

    return ans + len(right) + 1


nums = [1, 2, 5, 7, 5, 3, 4, 8, 9]

print(solution(nums))
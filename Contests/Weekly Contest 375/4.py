
def solution(nums):
    N = len(nums)
    d = {}
    MOD = 10 ** 9 + 7

    for idx, num in enumerate(nums):
        if num in d:
            d[num][1] = idx
        else:
            d[num] = [idx, idx]

    intervals = list(d.values())
    intervals.sort()
    print(intervals)

    l = intervals[0][0]
    r = intervals[0][1]
    count = 1

    for i in range(1, len(intervals)):
        if intervals[i][0] < r and intervals[i][1] > r:
            r = intervals[i][1]
        elif intervals[i][0] > r:
            count += 1
            l = intervals[i][0]
            r = intervals[i][1]
    print(count)
    ans = 1
    for i in range(count-1):
        ans = (ans * 2) % MOD

    return ans




# nums = [1,2,3,4]
# nums = [1,2,1,3]
# nums = [1,1,1,1]
nums = [1,6,8,1,5]

print(solution(nums))
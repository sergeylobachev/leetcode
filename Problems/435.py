def solution(intervals):
    intervals.sort()
    l = intervals[0][0]
    r = intervals[0][1]
    ans = 0
    print(intervals)

    for interval in intervals:
        if interval[0] < r:
            r = min(r, interval[1])
            ans += 1
        else:
            l = interval[0]
            r = interval[1]
    
    return ans-1


intervals1 = [[1,2],[2,3],[3,4],[1,3]]  # 1
intervals2 = [[1,2],[1,2],[1,2]]  # 2
intervals3 = [[1,2],[2,3]] # 0


print(solution(intervals1))
print(solution(intervals2))
print(solution(intervals3))
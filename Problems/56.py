def solution(intervals):

    intervals.sort()
    ans = []
    l = intervals[0][0]
    r = intervals[0][1]

    for i in range(0, len(intervals)):
        if intervals[i][0] <= r:
            r = max(r, intervals[i][1])
            if i == len(intervals) - 1:
                ans.append([l, r])
        else:
            ans.append([l, r])
            l = intervals[i][0]
            r = intervals[i][1]
            if i == len(intervals) - 1:
                ans.append([l, r])

        print(f"i={i}, {l}, {r}")


    return ans



intervals = [[1,4],[4,5]]
# intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution(intervals))


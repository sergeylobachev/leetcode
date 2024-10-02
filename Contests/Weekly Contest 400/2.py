
def solution(days, meetings):

    meetings.sort()
    r = 0
    ans = 0
    maxright = -1
    for i in range(len(meetings)):
        nl = meetings[i][0]
        nr = meetings[i][1]
        maxright = max(nr, maxright)
        if nl <= r and nr > r:
            r = nr
            continue
        if nl > r:
            print(nl, nr)
            ans += nl - r - 1
            l = nl
            r = nr
    ans += days - maxright
    return ans

days = 10
meetings = [[5,7],[1,3],[9,10]]

days = 5
meetings = [[2,4],[1,3]]

days = 57
meetings = [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]]


print(solution(days, meetings))

    

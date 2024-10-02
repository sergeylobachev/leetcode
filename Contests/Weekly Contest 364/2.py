def solution(heights):
    N = len(heights)
    ans = 0

    for i in range(N):
        cursum = heights[i]
        l = i - 1
        curleft = heights[i]
        curright = heights[i]

        while l >= 0:
            if heights[l] >= curleft:
                cursum += curleft
                l -= 1
            else:
                curleft = min(heights[l], curleft)
                cursum += curleft
                l -= 1

        r = i + 1
        while r < N:
            if heights[r] >= curright:
                cursum += curright
                r += 1
            else:
                curright = min(heights[r], curright)
                cursum += curright
                r += 1
        
        ans = max(ans, cursum)

    return ans



heights = [5,3,4,1,1]
heights = [6,5,3,9,2,7]
heights = [3,2,5,5,2,3]


print(solution(heights))
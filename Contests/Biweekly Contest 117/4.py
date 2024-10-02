def solution(values):
    rows = len(values)
    cols = len(values[0])

    ans = 0

    ends = [0 for _ in range(rows)]

    ## [value, row]
    for i in range(rows):
        ends[i] = (values[i][-1], i, cols-1)

    for i in range(1, rows*cols + 1):
        val, idx, jdx = min(ends)
        ans += i * val
        ends.remove(min(ends))
        if jdx > 0:
            ends.append((values[idx][jdx-1], idx, jdx-1))


    print(ends)
    return ans


values = [[8,5,2],[6,4,1],[9,7,3]]

print(solution(values))
 

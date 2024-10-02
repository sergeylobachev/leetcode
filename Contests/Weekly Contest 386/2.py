


def overlap(a,b,c,d):
    if d <= a or c >= b:
        return 0
    if c <= a and d >= b:
        return b-a
    if c >= a and d <= b:
        return d-c
    if c <= a and d <= b:
        return d-a
    if c >= a and d >= b:
        return b-c
    

def solution(bottomLeft, topRight):
    answer = 0
    for i in range(len(bottomLeft)):
        for j in range(i+1, len(bottomLeft)):
            w = overlap(bottomLeft[i][0], topRight[i][0], bottomLeft[j][0], topRight[j][0])
            h = overlap(bottomLeft[i][1], topRight[i][1], bottomLeft[j][1], topRight[j][1])
            answer = max(answer, min(h,w) ** 2)

    return answer


bottomLeft = [[1,1],[2,2]]
topRight = [[4,4],[4,4]]

# bottomLeft = [[1,1],[2,2],[3,1]]
# topRight = [[3,3],[4,4],[6,6]]

# bottomLeft = [[1,1],[2,2],[1,2]]
# topRight = [[3,3],[4,4],[3,4]]

# bottomLeft = [[1,1],[3,3],[3,1]]
# topRight = [[2,2],[4,4],[4,2]]

print(solution(bottomLeft, topRight))
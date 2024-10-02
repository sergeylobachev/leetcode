matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = [["]]

def solution(matrix):

    answer = 0

    rows = len(matrix)
    cols = len(matrix[0])

    adm = [[0] * (cols+1) for i in range(rows+1)]

    for i in range(1, rows+1):
        for j in range(1, cols+1):
            adm[i][j] = adm[i][j-1] + adm[i-1][j] - adm[i-1][j-1]
            adm[i][j] += int(matrix[i-1][j-1])


    for i in range(1, rows+1):
        for j in range(1, cols+1):
            k = 1
            while (i + k <= rows + 1) and (j + k <= cols + 1) and (adm[i+k-1][j+k-1] - adm[i+k-1][j-1] - adm[i-1][j+k-1] + adm[i-1][j-1] == k * k):
                answer = max(answer, k*k)
                k += 1

    return answer

print(solution(matrix))
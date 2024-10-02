matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

## we replzed one with zero in bottom right corner

def solution(matrix):
    answer = 0

    rows = len(matrix)
    cols = len(matrix[0])

    adm = [[0] * (cols+1) for i in range(rows+1)]

    ## creating addictive matrix that we'll use as a helper
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            adm[i][j] = adm[i-1][j] + adm[i][j-1] - adm[i-1][j-1]
            adm[i][j] += matrix[i-1][j-1]

    for i in range(1, rows+1):
            for j in range(1, cols+1):
                k = 1
                while (i + k <= rows+1) and (j + k <= cols+1) and adm[i+k-1][j+k-1] - adm[i+k-1][j-1] - adm[i-1][j+k-1] + adm[i-1][j-1] == k * k:                
                    answer += 1
                    # print(f"i={i}, j={j}, k={k}")
                    k += 1

    return answer

print(solution(matrix))
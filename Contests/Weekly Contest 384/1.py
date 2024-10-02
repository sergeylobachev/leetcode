def solution(matrix):
    R = len(matrix)
    C = len(matrix[0])

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == -1:
                m = float("-inf")
                for k in range(R):
                    if matrix[k][j] > m:
                        m = matrix[k][j]
                matrix[i][j] = m

    return matrix


matrix = [[3,-1],[5,2]]

print(solution(matrix))
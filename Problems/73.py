def solution(matrix):
    R = len(matrix)
    C = len(matrix[0])

    if matrix[0][0] == 0:
        matrix[0][0] = [0, 0]
    else:
        matrix[0][0] = [1, 1, matrix[0][0]]

    for j in range(1, C):
        if matrix[0][j] == 0:
            matrix[0][0][0] = 0
    
    for i in range(1, R):
        if matrix[i][0] == 0:
            matrix[0][0][1] = 0

    for i in range(1, R):
        for j in range(1, C):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, R):
        for j in range(1, C):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if matrix[0][0][0] == 0:
        for j in range(1, C):
            matrix[0][j] =0

    if matrix[0][0][1] == 0:
            for i in range(1, R):
                matrix[i][0] = 0

    if matrix[0][0][0] == 0 or matrix[0][0][1] == 0:
        matrix[0][0] = 0
    else:
        matrix[0][0] = matrix[0][0][2]

    return matrix


matrix = [[-1],[2],[3]]

print(solution(matrix))
def solution(matrix):
    matrix = list(zip(*matrix))
    matrix = [list(row) for row in matrix]
    for row in matrix:
        for i in range(len(row)//2):
            row[i], row[len(row)-i-1] = row[len(row)-i-1], row[i]
            
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution(matrix))
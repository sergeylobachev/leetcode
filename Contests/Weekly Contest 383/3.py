def solution(image, threshold):
    R = len(image)
    C = len(image[0])

    h = [[-1 for _ in range(C)] for _ in range(R)]
    a = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R-2):
        for j in range(C-2):
            if isgood(i, j):
                h[i][j] = mysum(i, j)

    for i in range(R):
        for j in range(C):
            s = 0
            c = 0
            for k in range(i-2, i+1):
                for l in range(j-2, j+1):
                    if k >= 0 and l >= 0 and h[k][l] > 0:
                        s += h[k][l]
                        c += 1
                        print(f"s and c")

            if c > 0: 
                a[i][j] = s // c
            else: 
                a[i][j] = image[i][j]

    return a

def isgood(r, c):

    for i in range(r, r+3):
        for j in range(c, c+2):
            if abs(image[i][j] - image[i][j+1]) > threshold:
                return False
    for j in range(c, c+3):
        for i in range(r, r+2):
            if abs(image[i][j] - image[i+1][j]) > threshold:
                return False
    
    return True


def mysum(r, c):
    s = 0
    for i in range(r, r+3):
        for j in range(c, c+3):
            s += image[i][j]

    return s // 9





# image = [[5,6,7,10],[8,9,10,10],[11,12,13,10]]
# threshold = 3

# image = [[5,6,7],[8,9,10],[11,12,13]]
# threshold = 1

image = [[10,20,30],[15,25,35],[20,30,40],[25,35,45]]
threshold = 12

print(solution(image, threshold))
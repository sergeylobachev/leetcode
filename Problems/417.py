def solution(heights):
    R = len(heights)
    C = len(heights[0])

    pl = set()
    al = set()

    def bfs(cell, land):
        x, y = cell
        land.add(cell)
        offsets = [(0,1), (0,-1), (1,0), (-1,0)]
        for o in offsets:
            xn = x + o[0]
            yn = y + o[1]
            if 0 <= xn < R and 0 <= yn < C and heights[xn][yn] >= heights[x][y] and (xn, yn) not in land:
                bfs((xn, yn), land)


    for i in range(R):
        bfs((i, 0), pl)
        bfs((i, C-1), al)

    for j in range(C):
        bfs((0, j), pl)
        bfs((R-1, j), al)

    return list(pl.intersection(al))

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(solution(heights))
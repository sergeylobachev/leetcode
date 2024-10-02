def solution(N, P):
    al = [[] for _ in range(N)]

    for course, precourse in P:
        al[precourse].append(course)

    color = ["white"] * N
    parent = [None] * N
    discovered = [0] * N
    finished = [0] * N

    answer = []
    hasCycle = False

    def visit(al, u):
        nonlocal time
        nonlocal hasCycle
        time += 1
        discovered[u] = time
        color[u] = "gray"
        for v in al[u]:
            if color[v] == "gray":
                hasCycle = True
            elif color[v] == "white":
                parent[v] = u
                visit(al, v)
        time += 1
        finished[u] = time
        color[u] = "black"
        answer.append(u)
            
    time = 0
    for u in range(N):
        if color[u] == "white":
            visit(al, u)

    if hasCycle == True:
        return -1

    # print("d", discovered)
    # print("f", finished)
    # print("p", parent)

    return answer[::-1]


N = 4
P = [[1,0],[2,0],[3,1],[3,2]]
print(solution(N, P))


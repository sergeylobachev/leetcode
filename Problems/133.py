def solution(numCourses, prerequisites):
    V = numCourses
    vertices = ["white"] * V 

    al = [[] for _ in range(V)]

    for x, y in prerequisites:
        al[y].append(x)

    f = 1
    time = 0

    def visit(al, u):
        nonlocal f
        color[u] = "gray"
        for v in al[u]:
            if color[v] == "gray":
                f = 0
                print("answer is False")
            if color[v] == "white":
                visit(al, v)

        color[u] = "black"

    N = len(al)
    color = ["white"] * N
    print(al, color)

    for u in range(N):
        if color[u] == "white":
            visit(al, u)

    return bool(f)


numCourses = 2
prerequisites = [[1,0],[0,1]]

# numCourses = 2
# prerequisites = [[1,0]]

# numCourses = 5
# prerequisites = [[1,4],[2,4],[3,1],[3,2]]

print(solution(numCourses, prerequisites))


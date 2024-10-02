def solution(av, bv):
    delta = 0
    N = len(av)
    A = [(av[i] + bv[i], av[i], bv[i]) for i in range(N)]
    A.sort(reverse=True)

    print(f"A= {A}")

    for i in range(N):
        if i % 2 == 0:
            delta += A[i][1]
        else:
            delta -= A[i][2]
        print(f"{i}, {delta}")

    if delta == 0:
        return 0
    elif delta > 0:
        return 1
    else:
        return -1


av = [1,3]
bv = [2,1]

print(solution(av, bv))
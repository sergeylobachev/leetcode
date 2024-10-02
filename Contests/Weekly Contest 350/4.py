def solution(cost, time):
    N = len(cost)

    def go(i, remain):
        if i >= N:
            return 10 ** 20

        # early termination
        if remain <= 0:
            return 0

        #pick
        pick = cost[i] + go(i+1, remain - time[i] - 1)

        #not_pick
        not_pick = go(i+1, remain)

        return min(pick, not_pick)


    return go(0, N)


cost = [1,2,3,2]
time = [1,2,3,2]

# cost = [2,3,4,2]
# time = [1,1,1,1]

print(solution(cost, time))
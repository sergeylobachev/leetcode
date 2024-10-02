def solution(gas, cost):
    N = len(gas)
    candidate = 0
    station = 0
    tank = 0
    distance = 0

    while candidate < N:
        print(f"candidate={candidate}, station={station}, tank={tank}, distance={distance}")
        tank += gas[station % N]
        tank -= cost[station % N]
        if tank >= 0:
            station += 1
            distance += 1
            if distance == N:
                return candidate
        else:
            tank = 0
            distance = 0
            station += 1
            candidate = station

    return -1

gas = [3,3,4]
cost = [3,4,4]

print(solution(gas, cost))
numBottles = 13
numExchange = 6


def solution(numBottles, numExchange):
    answer = numBottles
    empty = numBottles

    while empty >= numExchange:
        empty -= numExchange - 1
        answer += 1
        numExchange += 1

    return answer

print(solution(numBottles, numExchange))

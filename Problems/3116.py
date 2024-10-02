from math import lcm

def solution(coins, k):


    return answer


def calc(coins, n):
    N = len(coins)

    count_plus = 0
    count_minus = 0

    for mask in range(1, 1 << N):
        mylcm = 1
        sign = 0
        for i in range(N):
            if (mask & (1 << i)) > 0:
                mylcm = lcm(mylcm, coins[i])
                # print(f"mask={mask}, i={i}, mylcm={mylcm}")
                sign += 1
        # print(f"mask={mask}, mylcm={mylcm}")

        if sign % 2 == 0:
            count_minus += n // mylcm
        else:
            count_plus += n // mylcm
        # print(f"mask={mask}, {count_plus}, {count_minus}")

    return count_plus - count_minus

coins = [3, 6, 9]

print(calc(coins, 9))


l = 1
r = 10 ** 12

while l <= r:
    m = (l + r ) // 2
    if calc(coins, m) >= k:
        r = m- 1
    else:
        l = m + 1

    return l

    
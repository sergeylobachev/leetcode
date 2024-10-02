def solution(power, damage, health):
    ## (priority, damage, lives)

    N = len(damage)
    p = []
    for i in range(N):
        lives = health[i] // power + (health[i] % power > 0)
        p.append([damage[i] / lives, damage[i], lives])

    p.sort(reverse = True)

    ans = 0
    t = 0
    for i in range(N):
        t += p[i][2]
        ans += p[i][1] * t

    return ans

power = 4
damage = [1,2,3,4]
health = [4,5,6,8]

power = 1
damage = [1,1,1,1]
health = [1,2,3,4]

power = 8
damage = [40]
health = [59]

print(solution(power, damage, health))
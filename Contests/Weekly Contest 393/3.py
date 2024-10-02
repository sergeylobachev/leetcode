def solution(coins, k):

    curnum = 1
    counter = 0

    while True:
        for i in range(len(coins)):
            if curnum % coins[i] == 0:
                counter += 1
                break
        if counter == k:
            return curnum
        curnum += 1


coins = [5,2]
k = 7

print(solution(coins, k))
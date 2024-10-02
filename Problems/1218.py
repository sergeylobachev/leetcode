from collections import defaultdict

arr = [1,2,3,4]
difference = 1

def solution(arr, difference):
    d = defaultdict(int)
    dp = 0
    cur = 0
    for i in range(len(arr)):
        if (arr[i] - difference) in d.keys():
            cur = d[arr[i] - difference] + 1
            d[arr[i]] = cur
        else:
            cur = 1
            d[arr[i]] = cur
        
        dp = max(dp, cur)

    return dp

print(solution(arr, difference))
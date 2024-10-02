from collections import defaultdict

def solution(nums):
    MOD = 10 ** 9 + 7
    N = len(nums)
    dp_prv = defaultdict(int)
    dp_prv[0, 50] = 1

    for i in range(N):
        dp_cur = defaultdict(int)
        for up in range(0, nums[i] + 1):
            down = nums[i] - up
            for a, b in dp_prv:
                if up >= a and down <= b:
                    dp_cur[up, down] += dp_prv[a, b] % MOD

        dp_prv = dp_cur

    return sum(dp_cur.values()) % MOD


nums = [2,3,2]
# nums = [5,5,5,5]
print(solution(nums))





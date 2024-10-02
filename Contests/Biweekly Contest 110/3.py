from collections import defaultdict

def solution(nums):
    d = defaultdict(list)
    N = len(nums)

    for i in range(N):
        d[nums[i]].append(i)

    distances = []

    for key in d.keys():
        mx = 0
        a = d[key]
        l = len(a)
        for i in range(1, l):
            mx = max(mx, a[i] - a[i-1] -1)
        
        mx = max(mx, a[0] + N - a[-1] - 1)
        distances.append(mx)
    
    mn = min(distances)
    if mn % 2 == 0:
        return mn // 2
    else:
        return mn // 2 + 1



nums = [1,2,1,2]
nums = [2,1,3,3,2]
# nums = [5,5,5,5]

print(solution(nums))
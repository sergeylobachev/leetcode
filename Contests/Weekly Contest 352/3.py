from collections import defaultdict

def solution(nums):
    ans = 0
    d = defaultdict(int)

    for i, num in enumerate(nums):
        nd = defaultdict(int)
        nd[num, num] += 1

        for l, r in d.keys():
            if abs(num-l) > 2 or abs(num-r) > 2:
                pass
            else:
                if num < l:
                    nd[num, r] += d[l, r]
                elif l <= num <= r:
                    nd[l, r] += d[l, r]
                else:
                    nd[l, num] += d[l, r]

        d = nd
        ans += sum([d[key] for key in d.keys()])
        print(d, ans)

    return ans

nums = [5,4,2,4]
# nums = [1,2,3]

print(solution(nums))
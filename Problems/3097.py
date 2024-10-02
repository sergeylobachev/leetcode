# nums = [1,2,3]
# k = 2

nums = [2, 1, 8]
k = 10

# nums = [2,1,9,12]
# k = 21

def to_k(sum):
    pow = 0
    k = 0
    for i in range(32):
        if sum[i] > 0:
            k += 2 ** pow
        pow += 1
    return k


def solution(nums, k):
    sum = [0] * 32
    ans = len(nums) + 1
    l = 0
    r = 0

    while r < len(nums):
        for i in range(32):
            if nums[r] & (1 << i) > 0:
                sum[i] += 1

        if to_k(sum) >= k:
            while to_k(sum) >= k:
                for i in range(32):
                    if nums[l] & (1 << i) > 0:
                        sum[i] -= 1
                ans = min(ans, r-l+1)
                print(f"l={l}, r={r}, ans= {ans}, {sum}, {to_k(sum)}")
                l += 1
            sum = [0] * 32
            l += 1
            r = l

        else:
            r += 1

        print(f"l={l}, r={r}, ans= {ans}, {sum}, {to_k(sum)}")

    return ans

print(solution(nums, k))
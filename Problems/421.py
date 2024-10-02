def solution(nums):
    node = {}
    for num in nums:
        cur = node
        for i in range(32, -1, -1):
            if num & 1 << i > 0:
                bit = 1
            else: 
                bit = 0
            if bit in cur:
                cur = cur[bit]
            else:
                cur.update({bit: {}})
                cur = cur[bit]

    mx = 0
    for num in nums:
        curmax = 0
        cur = node
        for j in range(32, -1, -1):
            if num & 1 << j > 0:
                bit = 1
            else: 
                bit = 0
            if (1-bit) in cur:
                curmax += (1 << j)
                cur = cur[1-bit]
            else:
                cur = cur[bit]

        mx = (max(mx, curmax))

    return mx


nums = [3,10,5,25,2,8]

print(solution(nums))
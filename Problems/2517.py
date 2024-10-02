

def can(price, n, k):
    cur = 0
    count = 0

    for p in price:
        if p >= cur:
            count += 1
            cur = p + n

    return count >= k









price = [13,5,1,8,21,2]
price.sort()
k = 3

print(can(price, 8, 3))
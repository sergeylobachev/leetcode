def canship(capacity, weights, days):
    cursum = 0
    d = 0
    for i in range(len(weights)):
        cursum += weights[i]
        if cursum > capacity:
            d += 1
            cursum = weights[i]
    if cursum > 0: d += 1
    return d <= days


weights = [1,2,3,4,5,4,6,8,8,9,10]
days = 5
capacity = 15

print(canship(capacity, weights, days))
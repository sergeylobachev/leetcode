def solution(n, k, budget, composition, stock, cost):

    def possible(x):
        for comp in composition:
            totalcost = 0
            resource = [c*x for c in comp]
            for i in range(n):
                if resource[i] > stock[i]:
                    totalcost += (resource[i] - stock[i]) * cost[i]

            if totalcost <= budget:
                return True
            
        return False


    l = 0
    r = 10 ** 9

    while l < r:
        m = (r + l ) // 2
        if possible(m):
            l = m+1
        else:
            r = m

    return l-1

n = 3
k = 2
budget = 15
composition = [[1,1,1],[1,1,10]]
stock = [0,0,0]
cost = [1,2,3]

print(solution(n, k, budget, composition, stock, cost))


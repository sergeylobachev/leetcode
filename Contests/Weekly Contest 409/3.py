from collections import defaultdict

def solution(n, queries):

    d = defaultdict(int)
    for i in range(n-1):
        d[i] = i+1
    print(d)
    ans = []

    for a, b in queries:
        s = a

        while s < b:
            if s in d:
                ns = d[s]
                del d[s]
                s = ns
            elif s not in d:
                break
        else:
            d[a] = b
        ans.append(len(d.keys()))
        print(d)

    return ans

n = 5
queries = [[2,4],[0,2],[0,4]]

# n = 4
# queries = [[0,3],[0,2]]

# n = 5
# queries = [[1,4],[2,4]]

print(solution(n, queries))
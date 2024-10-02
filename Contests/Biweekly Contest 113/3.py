from collections import defaultdict

def solution(coordinates, k):
    ans = 0
    dict = defaultdict(int)

    for a, b in coordinates:
        for i in range(k+1):
            c = a ^ i
            d = b ^ (k-i)
            if (c,d) in dict:
                ans += dict[(c,d)]
        dict[(a,b)] += 1


    return ans


coordinates = [[1,2],[4,2],[1,3],[5,2]]
k = 5

coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]]
k = 0

print(solution(coordinates, k))
def solution(s, k):
        N = len(s)
        k = k % N
        doubles = s + s
        
        return doubles[k: k+N]




s = "byd"
k = 4
print(solution(s, k))
##expected ydb
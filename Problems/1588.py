arr = [1,4,2,5,3]
    
def solution(arr):  
    sum = 0
    n = len(arr)
    for i in range(n):
        a = ((i+1)//2) * ((n-i)//2)
        b = ((i+2)//2) * ((n-i+1)//2)
        sum += arr[i] * (a + b)
        print(arr[i], a)
    return int(sum)

print(solution(arr))



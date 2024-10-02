def solution(num):
    num = num[::-1]
    N = len(num)
    print(num)



    z = len(num)
    zf = 0
    for i in range(N):
        if num[i] == "0" and zf == 0:
            zf = 1
        elif num[i] == "0" and zf == 1:
            z = i - 1
            break
        elif num[i] == "5" and zf == 1:
            z = i - 1
            break
    
    f = len(num)
    ff = 0
    for i in range(N):
        if num[i] == "5":
            ff = 1
        elif num[i] == "2" and ff == 1:
            f = i - 1
            break
        elif num[i] == "7" and ff == 1:
            f = i - 1
            break
    
    x = len(num)
    for i in range(N):
        if num[i] == "0":
            x -= 1

            
    return min(z, f, x)

num = "2245047"
num = "2908305"
# num = "10"
print(solution(num))

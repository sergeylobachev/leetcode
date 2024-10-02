import functools

def comp(a, b):
    a = str(a)
    b = str(b)
    for i in range(min(len(a), len(b))):
        if int(a[i]) > int(b[i]):
            return 1
        if int(a[i]) < int(b[i]):
            return -1
    
    if len(a) == len(b):
        return 0
    elif (len(a) > len(b) and int(a[i+1]) > int(b[0])) or (len(b) > len(a) and int(b[i+1]) < int(a[0])):
        return 1
    else:
        return -1
    


nums =[8308,8308,830]

print(comp(8308, 830))



# nums.sort(key=functools.cmp_to_key(comp), reverse=True)
# ans =""
# for num in nums:
#     ans += str(num)
# print(ans)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a 




def solution(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    gcd = 0

    def isDivider(str, divider):
        ls = len(str)
        ld = len(divider)
        k = ls // ld
        for i in range(0, ls, ld):
            if str[i:i+ld] != divider:
                return False    

        return True

    for i in range(1, min(l1, l2)+1):
        print(i)
        if l1 % i == 0 and l2 % i == 0:
            if isDivider(str1, str1[:i]) and isDivider(str2, str1[:i]):
                gcd = max(gcd, i)

    return str1[:gcd]




str1 = "ABCABC"
str2 = "ABC"

print(solution(str1, str2))
print(gcd(7, 35))
print(gcd(35, 7))
print(gcd(1, 7))
print(gcd(1, 0))
print(gcd(0, 5))
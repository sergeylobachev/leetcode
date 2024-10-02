x = 100

def solution(x):
    sum_of_digits = 0
    s = x

    while s > 0:
        digit = s % 10
        s = s // 10
        sum_of_digits += digit

    if x % sum_of_digits == 0:
        return sum_of_digits
    else:
        return -1

print(solution(18))

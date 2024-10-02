def solution(a, b):
    la = len(a)
    lb = len(b)
    s = ""
    carry = 0
    for i in range(1, max(la, lb)+1):

        cur_digit = 0
        if la - i >= 0:
            cur_digit += int(a[-i])

        if lb - i >= 0:
            cur_digit += int(b[-i])

        cur_digit += carry

        s += str(cur_digit % 2)
        if cur_digit >= 2:
            carry = 1
        else:
            carry = 0
        
        print(f"step {i}, cur_digit is {cur_digit}, carry is {carry}")

    if carry: s += "1"

    return s[::-1]



a = "11"
b = "1" 
print(solution(a, b))


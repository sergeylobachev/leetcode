def solution(s):
    sign = 1 ## sign
    strNumber = ""
    
    for i in range(len(s)):
        if s[i] == " ":
            pass
        elif s[i] == "-":
            sign = -1
            i += 1
            break
        elif s[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            sign = 1
            break
        else:
            return 0


    lz = 1
    for j in range(i, len(s)):
        if s[j] == "0" and lz == 1:
            pass
        elif s[j] == "0" and lz == 0:
            strNumber += s[j]
        elif s[j] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            strNumber += s[j]
            lz = 0
        else:
            break
    
    if len(strNumber) == 0:
        return 0
    number = int(strNumber) * sign

    # if number < -2 ** 31 - 1: 
    #     print("chlen")
    #     number == -2 ** 31
    # if number > 2 ** 31 - 1:
    #     number = 2 ** 31 - 1
    

    return number


s = "-2147483649"
print(solution(s))

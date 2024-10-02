def triplet(num):

    ## consider triplet to be abc 

    sd = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        0: "Zero"
    }

    dd = {
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Fourty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
    }

    c = num % 10
    b = ((num - c) // 10) % 10
    a = num // 100

    s = ""
    if a > 0:
        s += sd[a] + " Hundred"

    if b > 0:
        if (10 * b + c) in dd:
            if a > 0:
                s += " " + dd[10 * b + c]
            else:
                s += dd[10 * b + c]
            return s
        
        elif 10 * b in dd:
            if a > 0:
                s += " " + dd[10 * b]
            else:
                s += dd[10 * b]

    if c > 0:
        if a > 0 or b > 0:
            s += " " + sd[c]
        else:
            s += sd[c]

    return s

def solution(num):
    d = {
        10**9: "Billion",
        10**6: "Million",
        10**3: "Thousand"
    }


    if num == 0:
        return "Zero"

    s = ""

    R = num % 10**3
    T = (num  // 10 ** 3) % 10**3
    M = (num  // 10 ** 6) % 10**3
    B = (num  // 10 ** 9) % 10**3

    print(B, M, T, R)

    if B > 0:
        s += triplet(B) + " Billion"
    
    if M > 0:
        if B > 0:
            s += " " + triplet(M) + " Million"
        else:
            s += triplet(M) + " Million"

    if T > 0:
        if B > 0 or M > 0:
            s += " " + triplet(T) + " Thousand"
        else:
            s += triplet(T) + " Thousand"

    if R > 0:
        if B > 0 or M > 0 or T > 0:
            s += " " + triplet(R)
        else:
            s += triplet(R)

    return s




    



columnNumber = 701

s = ""
while columnNumber > 0:
    if columnNumber % 26 == 0:
        s += "Z"

    else:
        letter = chr(64 + columnNumber % 26)
        s += letter
        columnNumber = int((columnNumber // 26) - columnNumber % 26)
    print(columnNumber)

print(s)
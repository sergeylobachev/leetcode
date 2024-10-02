def solution(rows, cols, rStart, cStart):

    dir = "E"
    ans = []
    ans.append([rStart, cStart])

    r = rStart
    c = cStart
    remaining = rows * cols - 1
    leg_len = 1
    rem_leg = 1

    while remaining > 0:
        step = 0
        if dir == "E":
            if rem_leg > 0:
                c += 1
                rem_leg -= 1
                step = 1
            else:
                dir = "S"
                rem_leg = leg_len
        
        elif dir == "S":
            if rem_leg > 0:
                r += 1
                rem_leg -= 1
                step = 1
            else:
                dir = "W"
                leg_len += 1
                rem_leg = leg_len

        elif dir == "W":
            if rem_leg > 0:
                c -= 1
                rem_leg -= 1
                step = 1
            else:
                dir = "N"
                rem_leg = leg_len

        elif dir == "N":
            if rem_leg > 0:
                r -= 1
                rem_leg -= 1
                step = 1
            else:
                dir = "E"
                leg_len += 1
                rem_leg = leg_len


        if step == 1:
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r,c])
                remaining -= 1

        # if step == 1:
        #     print(r, c," ", leg_len)

    return ans


rows = 5
cols = 6
rStart = 1
cStart = 4

print(solution(rows, cols, rStart, cStart))
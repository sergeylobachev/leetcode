def solution(day, month, year):
    def UnixDays(d, m, y):
        mDict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        dayOfTheYear = 0

        for i in range(1, m):
            dayOfTheYear += mDict[i]

        dayOfTheYear += d
        if y % 4 == 0 and y % 100 != 0 and m >= 3:
            dayOfTheYear += 1

        # leapDays = (y - 1971) // 4 + 1
        leapDays = (y - 1969) // 4 - (y == 2100)
        return (y - 1970) * 365 + leapDays + dayOfTheYear

    dDict = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}

    return dDict[(UnixDays(day, month, year) + 3) % 7]


print(solution(15, 8, 1993))


def solution(n):


    def isp(array):
        N = len(array)
        for i in range(N//2):
            if array[i] != array[N-1-i]:
                return False
        return True

    def baseb(n, b):
        a = []
        while n > 0:
            d = n % b
            a.append(d)
            n = (n - d) // b

        return a

    for i in range(2, n-1):
        if not isp(baseb(n, i)):
            return False

    return True


print(solution(9))
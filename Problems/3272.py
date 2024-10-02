from math import comb

def solution(n, k):

    if n == 1:
        return sum([1 for x in range(1, 10) if x % k == 0])

    f = set()

    for i in range(10 ** (n//2-1), 10 ** (n//2)):
        i = str(i)

        if n % 2 == 0:
            candidate = i + i[::-1]
            if int(candidate) % k == 0:
                a = [0 for _ in range(10)]
                for c in candidate:
                    a[int(c)] += 1
                f.add(tuple(a))
        
        elif n % 2 == 1:
            for j in range(10):
                candidate = i + str(j) + i[::-1]
                if int(candidate) % k == 0:
                    a = [0 for _ in range(10)]
                    for c in candidate:
                        a[int(c)] += 1
                    f.add(tuple(a))

    ret = 0
    for freq in f:
        rem = n
        combinations = comb(rem-1, freq[0])
        rem -= freq[0]

        for i in range(1, 10):
            combinations *= comb(rem, freq[i])
            rem -= freq[i]

        ret += combinations

    return ret

    
print(solution(3, 5))
print(solution(1, 4))
print(solution(5, 6))


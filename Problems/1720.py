def solution(encoded, first):
    def helper(a, b):
            a = format(a, "#034b")[2:]
            b = format(b, "#034b")[2:]
            print(a, b)
            ans = 0
            for i in range(32):
                if (int(a[~i]) + int(b[~i])) % 2:
                    ans += 2 ** i

            return ans

    answer = []
    answer.append(first)

    for num in encoded:
        cur = helper(first, num)
        answer.append(cur)
        first = cur

    return answer


encoded = [1,2,3]
first = 1

encoded = [6,2,7,3]
first = 4
print(solution(encoded, first))
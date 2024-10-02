

def solution(expression):

    arr = []
    num = 0
    for c in expression:
        if c in "*+-":
            arr.append(num)
            arr.append(c)
            num = 0
        else:  
            num = num * 10 + int(c)
    arr.append(num)

    def calc(left, right):
        if left == right:
            return [arr[left]]

        ans = []
        for i in range(left+1, right, 2):
            left_ans = calc(left, i-1)
            right_ans = calc(i+1, right)

            if arr[i] == "*":
                for l in left_ans:
                    for r in right_ans:
                        ans.append(r*l)

            if arr[i] == "+":
                for l in left_ans:
                    for r in right_ans:
                        ans.append(r+l) 

            if arr[i] == "-":
                for l in left_ans:
                    for r in right_ans:
                        ans.append(l-r)

        return ans

    return calc(0, len(expression)-1)

print(solution("2-1-1"))
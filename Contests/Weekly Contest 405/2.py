def solution(n):

    answer = ["0", "1"]

    for i in range(n-1):
        newanswer = set()
        for s in answer:
            if s[-1] == "0":
                newanswer.add(s+"1")
            else:
                newanswer.add(s+"0")
                newanswer.add(s+"1")

        answer = newanswer

    return answer



print(solution(1))
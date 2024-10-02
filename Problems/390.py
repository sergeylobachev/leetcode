

def solution(index, n, jumplen, direction):
    if direction == "r":
        index += jumplen * ((n-index) // jumplen)
        if index - jumplen < 1:
            return index
        return solution(index-jumplen, n, jumplen * 2, "l")

    elif direction == "l":
        index -= jumplen * ((index - 1) // jumplen)
        if index + jumplen > n:
            return index
        return solution(index+jumplen, n, jumplen * 2, "r")


print(solution(2, 10, 2, "r"))



def solution(s1, s2, x):

    N = len(s1)
    s = [0] * N

    for i in range(N):
        if s1[i] != s2[i]:
            s[i] = 1

    counter = sum(s)
    if counter % 2:
        return -1
    print(s)
    l = 0 
    r = 1
    answer = 0
    while r < N:
        if s[l] == s[r] == 1:
            if r - l >= x:
                l = r 
                r = l + 1
            else:
                answer += (r - l)
                counter -= 2
                l = r + 1
                r = l + 1
        else:
            if s[l] != 1:
                l += 1
                r += 1
            elif s[r] != 1:
                r += 1
        # print(f"l={l}, r={r}, answer={answer}, counter={counter}")
    return answer + (counter // 2) * x


s1 = "1100011000"
s2 = "0101001010"
x = 2


s1 = "01111101010100110100"
s2 = "10010011011001011000"
x = 21

s1 = "11001011111"
s2 = "01111000110"
x = 2

s1 = "0110010001101011010"
s2 = "1011110101000001100"
x = 3

print(solution(s1, s2, x))
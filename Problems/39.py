def solution(candidates, target):
    N = len(candidates)
    candidates.sort()
    answer = []

    def dfs(index, target, array):
        if index == N:
            return
            
        c = candidates[index]

        if c == target:
            answer.append(array + [c])
        if c < target:
            dfs(index, target-c, array + [c])
            dfs(index+1, target, array)

    dfs(0, target, [])

    return answer

    
    
candidates = [2,3,5]
target = 8


# candidates = [2]
# target = 1


# candidates = [2,3,6,7]
# target = 7

print(solution(candidates, target))
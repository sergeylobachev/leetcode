def solution(nums, queries):
    sm = sum(nums)
    sortnums = [(nums[i], i) for i in range(len(nums))]
    sortnums.sort()
    marked = set()
    answer = [] * len(queries)
    
    for idx, k in queries:
        if idx not in marked:
            sm -= nums[idx]
            marked.add(idx)
        while k > 0 and len(sortnums) > 0:
            elem = sortnums.pop(0)
            if elem[1] not in marked:
                sm -= elem[0]
                marked.add(elem[1])
                k -= 1
        answer.append(sm)

    return answer


nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]

nums = [1,4,2,3]
queries = [[0,1]]

print(solution(nums, queries))
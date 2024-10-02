

def solution(nums, queries, x):
    d = {}
    ans = [-1] * len(queries)

    counter = 1
    for i, num in enumerate(nums):
        if num == x:
            d[counter] = i
            counter += 1

    for i, q in enumerate(queries):
        if q in d:
            ans[i] = d[q]


    return ans




nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1

nums = [1,2,3]
queries = [10]
x = 5
print(solution(nums, queries, x))

from collections import defaultdict

def solution(limit, queries):

    colors = set()
    colorsFreq = defaultdict(int)
    ballsMap = defaultdict(int)
    ans = []

    for ball, new_color in queries:
        old_color = ballsMap[ball]

        if colorsFreq[old_color] == 1:
            colors.remove(old_color)
        
        colorsFreq[old_color] -= 1
        colorsFreq[new_color] += 1
        colors.add(new_color)
        ballsMap[ball] = new_color

        ans.append(len(colors))

    return ans
 


    
# limit = 4
# queries = [[1,4],[2,5],[1,3],[3,4]]

# limit = 4
# queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

# limit = 1
# queries = [[0,1],[0,4],[0,4],[0,1],[1,2]]


limit = 1
queries = [[0,2],[1,10],[0,10],[0,3],[1,5]]

print(solution(limit, queries))
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict


class SegmentTree:
    def __init__(self, data):
        self.len = len(data)
        self.size = 1 << (self.len - 1).bit_length()
        self.data = [0] * (2 * self.size)

        self.data[self.size: self.size + self.len] = data 
        for i in range(self.size-1, 0, -1):
            self.data[i] = max(self.data[i << 1], self.data[i << 1 | 1])

        print(self.data)

    def update(self, p, val):
        self.data[p + self.size] = val
        i = p + self.size

        while i > 1:
            self.data[i >> 1] = max(self.data[i], self.data[i ^ 1])
            i >>= 1

    def query(self, l, r) :  
        res = 0
        l += self.size 
        r += self.size
        
        while l < r: 
            if (l & 1): 
                res = max(res, self.data[l])
                l += 1
        
            if (r & 1): 
                r -= 1
                res = max(res, self.data[r])
                
            l >>= 1
            r >>= 1
        
        return res

def solution(nums1, nums2, queries):
    N = len(nums1)
    nums = [(nums1[i], nums2[i]) for i in range(N)]
    nums.sort()

    ## Using monotonic stack (ms) to keep inly dominant points
    ms = []
    for num in nums:
        while ms:
            x = num[0]
            y = num[1]
            if ms[-1][0] <= x and ms[-1][1] <= y:
                ms.pop()
            else:
                break

        ms.append(num)
    print(f"ms={ms}")

    ## x is the first coordinate of dominate points
    ## y is the second coordinate of dominate points
    ## s is the sum of x and y

    x = []
    y = []
    s = []
    ans = [0] * len(queries)

    for point in ms:
        x.append(point[0])
        y.append(point[1])
        s.append(point[0] + point[1])
    
    print(f"x={x}")
    print(f"y={y}")
    print(f"s={s}")
    y = y[::-1]
        
    st = SegmentTree(s)

    for i, (a, b) in enumerate(queries):
        l = bisect_left(x, a)
        r = len(x) - 1 - bisect_left(y, b)
        print(f"query={a, b} left={l}, right={r}")
        if l > r:
            ans[i] = -1
        else:
            ans[i] = st.query(l, r+1)

    return ans

nums1 = [4,3,1,2]
nums2 = [2,4,9,5]
queries = [[4,1],[1,3],[2,5]]

nums1 = [3,2,5]
nums2 = [2,3,4]
queries = [[4,4],[3,2],[1,1]]


nums1 = [2,1]
nums2 = [2,3]
queries = [[3,3]]

print(solution(nums1, nums2, queries))
































# nums1 = [31]
# nums2 = [17]
# queries = [[1,79]]

# nums1 = [18]
# nums2 = [40]
# queries = [[40,26],[89,31]]

# nums1 = [72,44]
# nums2 = [60,86]
# queries = [[33,14]]
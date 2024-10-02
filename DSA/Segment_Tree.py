class SegmentTree:

    def __init__(self, data):
        self.len = len(data)
        self.size = 1 << (self.len - 1).bit_length()
        self.data = [0] * (2 * self.size)

        self.data[self.size: self.size + self.len] = data 
        for i in range(self.size-1, 0, -1):
            self.data[i] = self.data[i << 1] + self.data[i << 1 | 1]

        print(self.data)

    def update(self, p, val):
        self.data[p + self.size] = val
        i = p + self.size

        while i > 1:
            self.data[i >> 1] = self.data[i] + self.data[i ^ 1]
            i >>= 1

    def query(self, l, r) :  
        res = 0
        l += self.size 
        r += self.size
        
        while l < r: 
            if (l & 1): 
                res += self.data[l]
                l += 1
        
            if (r & 1): 
                r -= 1
                res += self.data[r]
                
            l >>= 1
            r >>= 1
        
        return res


nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums = [1, 2, 3, 4, 5]
st = SegmentTree(nums)
print(st.query(3,6))
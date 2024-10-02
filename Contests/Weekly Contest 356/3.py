def merge(s1, s2):
    if s2 in s1:
        return s1
    l1 = len(s1)
    l2 = len(s2)
    l = min(l1, l2)
    for i in range(l, -1, -1):
        # print(s1[l1-i:], s2[:i])
        if s1[l1-i:] == s2[:i]:
            return s1 + s2[i:]
        
    return s1 + s2


print(merge("cac", "a"))

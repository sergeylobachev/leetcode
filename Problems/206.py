class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

d = LinkedList(4)
c = LinkedList(3, d)
b = LinkedList(2, c)
a = LinkedList(1, b)

print(a.val)
print(b.val)
print(c.val)
print(d.val)

print(not d.next)
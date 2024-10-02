from collections import defaultdict

d = defaultdict(int)

s = "abba"

for char in s:
    d[char] += 1

print(d)
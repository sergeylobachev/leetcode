from collections import defaultdict
from collections import Counter

s = defaultdict(int)
t = defaultdict(int)

s = "abcd"
t = "abcde"

ct = Counter(t)
cs = Counter(s)

print(
    set(ct.keys()).difference(set(cs.keys()))
)



from bisect import bisect_right
from bisect import bisect_left
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        a = [x for [x, y] in self.d[key]]
        idx = bisect_right(a, timestamp, 0)

        return self.d[key][idx-1][1] if idx > 0  else ""

obj = TimeMap()
obj.set("foo", "bar", 1)
obj.set("foo", "bar", 2)
obj.set("foo", "bar2", 3)
obj.get("foo", 2)


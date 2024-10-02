from collections import Counter

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]

q = []
for query in queries:
    cnt = Counter(query)
    q.append(cnt[min(cnt.keys())])

w = []
for word in words:
    cnt = Counter(word)
    w.append(cnt[min(cnt.keys())])


print(w)

class Trie:

    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        d = self.root
        for letter in word:
            d = d.setdefault(letter, {})
        d["_end_"] = True


    def search(self, word: str) -> bool:
        d = self.root
        for letter in word:
            if letter not in d:
                return False
            d = d[letter]
        return "_end_" in d

    def delitem(self, word: str) -> None:
        d = self.root
        nodes = [d]
        for letter in word:
            d = d[letter]
            nodes.append(d)
        del d["_end_"]

    
    def startsWith(self, prefix: str) -> bool:
        d = self.root
        for letter in prefix:
            if letter not in d:
                return False
            d = d[letter]


words = ["abc", "ark", "ab"]
T = Trie(*words)

print(T.root)
print(T.search("sgfg"))
T.delitem("abc")
print(T.root)
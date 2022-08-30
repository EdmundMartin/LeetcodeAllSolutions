

# Runtime: 120 ms, faster than 99.69% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 27.6 MB, less than 84.06% of Python3 online submissions for Implement Trie (Prefix Tree).
class Trie:

    def __init__(self):
        self.trie = {}
        self.end_char = "*"

    def insert(self, word: str) -> None:
        trie_node = self.trie
        for ch in word:
            if ch in trie_node:
                trie_node = trie_node[ch]
            else:
                trie_node[ch] = {}
                trie_node = trie_node[ch]
        trie_node[self.end_char] = None
        return

    def search(self, word: str) -> bool:
        trie_node = self.trie
        for ch in word:
            if ch not in trie_node:
                return False
            else:
                trie_node = trie_node[ch]
        return "*" in trie_node

    def startsWith(self, prefix: str) -> bool:
        trie_node = self.trie
        for ch in prefix:
            if ch not in trie_node:
                return False
            else:
                trie_node = trie_node[ch]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    contains = trie.search("apple")
    print(contains)
    starts_with = trie.startsWith("app")
    print(starts_with)


class Trie:
    def __init__(self):
        self.trie = {}

    def add_word(self, word: str):
        current_node = self.trie
        for ch in word:
            if ch not in current_node:
                current_node[ch] = {}
            current_node = current_node[ch]
        current_node["*"] = "END_WORD"

    def search_in_node(self, node, word) -> bool:
        current_node = node
        for idx, ch in enumerate(word):
            if ch not in current_node:
                if ch == ".":
                    for x in current_node:
                        if x != "*" and self.search_in_node(current_node[x], word[idx + 1:]):
                            return True
                return False
            current_node = current_node[ch]
        return "*" in current_node


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add_word(word)

    def search(self, word: str) -> bool:
        return self.trie.search_in_node(self.trie.trie, word)


if __name__ == '__main__':


    """
    ["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search"]
    [[], ["a"], ["a"], ["."], ["a"], ["aa"], ["a"], [".a"], ["a."]]
    """
    w = WordDictionary()
    w.addWord("a")
    w.addWord("a")
    w.search(".")
    w.search("aa")
    w.search("a")
    #w.search(".a")
    w.search("a.")

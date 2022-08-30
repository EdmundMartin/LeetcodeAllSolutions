from typing import List


class FileSystem:

    def __init__(self):
        self.trie = {}
        self.value_store = {}

    def determine_if_valid(self, parts: List[str]):
        valid = True
        trie_node = self.trie
        for part in parts:
            if part not in trie_node:
                return False
            trie_node = trie_node[part]
        return valid

    def insert_into_trie(self, parts: List[str]) -> bool:
        trie_node = self.trie
        new_path = False
        for part in parts:
            if part not in trie_node:
                trie_node[part] = {}
                trie_node = trie_node[part]
                new_path = True
            else:
                trie_node = trie_node[part]
        return new_path

    def createPath(self, path: str, value: int) -> bool:
        parts = path.lstrip('/').split('/')
        if len(parts) > 1:
            not_valid = self.determine_if_valid(parts[:-1])
            if not_valid is False:
                return not_valid
        new_path = self.insert_into_trie(parts)
        if new_path:
            self.value_store[path] = value
        return new_path

    def get(self, path: str) -> int:
        if path in self.value_store:
            return self.value_store[path]
        return -1


if __name__ == '__main__':
    """
    ["FileSystem","createPath","createPath","get","createPath","get"]
    [[],["/leet",1],["/leet/code",2],["/leet/code"],["/leet/code",3],["/leet/code"]]
    [null,true,true,2,false,2]
    """
    filesystem = FileSystem()
    res = filesystem.createPath("/leet", 1)
    assert res is True
    res = filesystem.createPath("/leet/code", 2)
    assert res is True
    res = filesystem.get("/leet/code")
    assert res == 2
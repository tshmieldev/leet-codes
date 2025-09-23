class TrieNode:
    def __init__(self, val=None, end=False, links=None):
        self.val = val
        self.end = end
        self.links = {} if links is None else links

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        dummy = self.trie
        for char in word:
            if char in dummy.links:
                pass
            else:
                dummy.links[char] = TrieNode(char, False)
            dummy = dummy.links[char]
        dummy.end = True

    def search(self, word: str) -> bool:
        dummy = self.trie
        i=0
        while dummy and i < len(word):
            dummy = dummy.links.get(word[i], None)
            i += 1
        if not dummy:
            return False
        return dummy.end

    def startsWith(self, prefix: str) -> bool:
        dummy = self.trie
        i=0
        while dummy and i < len(prefix):
            dummy = dummy.links.get(prefix[i], None)
            i += 1
        if not dummy:
            return False
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
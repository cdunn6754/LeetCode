import unittest

class TrieNode:
    def __init__(self, val=None, eow=False):
        self.val = val
        self.children = []
        self.eow = eow

    def get_eow_child_with_val(self, val):
        for n in self.children:
            if n.val == val and n.eow:
                return n
        return None
    
    def get_child_with_val(self, val):
        eow_n = None
        for n in self.children:
            if n.val == val and n.eow:
                eow_n = n
            elif n.val == val:
                return n
        return eow_n
    
    def get_child_vals(self):
        return [n.val for n in self.children]
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.first_row = self.root.children

    def r_search(self, s, n):
        cn = n.get_child_with_val(s)
        if not cn == None:
            return self.r_search(s[1:], cn)
        return n

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = self.root
        for l in word[0:-1]:
            cn = n.get_child_with_val(l)
            if cn == None or cn.eow:
                cn = TrieNode(l)
                n.children.append(cn)
            n = cn

        last_node = n.get_child_with_val(word[-1])
        if last_node == None or not last_node.eow:
            n.children.append(TrieNode(word[-1], eow=True))

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self.root
        for l in word[0:-1]:
            cn = n.get_child_with_val(l)
            if cn == None or cn.eow:
                return False
            n = cn

        last_node = n.get_eow_child_with_val(word[-1])
        if last_node == None:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = self.root
        for l in prefix:
            cn = n.get_child_with_val(l)
            if cn == None:
                return False
            n = cn
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class trieTest(unittest.TestCase):
    def setUp(self):
        self.t = Trie()
        self.t.insert("apple")
        
    def test_insert(self):
        self.assertIn("a", self.t.root.get_child_vals())
        self.assertNotIn("p", self.t.root.get_child_vals())

        a_node = self.t.root.get_child_with_val("a")
        self.assertIn("p", a_node.get_child_vals())

    def test_search(self):
        self.assertTrue(self.t.search("apple"))
        self.assertFalse(self.t.search("app"))

    def test_starts_with(self):
        self.assertTrue(self.t.startsWith("app"))

    def test_integration(self):
        self.t.insert("app")
        self.assertTrue(self.t.search("app"))
        
if __name__ == "__main__":
    unittest.main()

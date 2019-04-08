
import random, unittest
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elems = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. 
        Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            #import pdb; pdb.set_trace();
            self.elems.append(val)
            self.pos[val].add(len(self.elems) - 1)
            return False
        self.elems.append(val)
        self.pos[val] = {len(self.elems) - 1}
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. 
        Returns true if the set contained the specified element.
        """
        if not val in self.pos:
            return False

        if self.elems[-1] == val:
            self.elems.pop()
            self.pos[val].remove(len(self.elems))
            if len(self.pos[val]) == 0:
                self.pos.pop(val)
            return True

        swap_idx = self.pos[val].pop()
        swap_val = self.elems[-1]
        
        self.pos[swap_val].remove(len(self.elems) -1)
        self.pos[swap_val].add(swap_idx)

        
        self.elems[swap_idx], self.elems[-1] = self.elems[-1], self.elems[swap_idx]
        self.elems.pop()
        
        if len(self.pos[val]) == 0:
            self.pos.pop(val)
            
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.elems)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class dsTest(unittest.TestCase):
    # def test_1(self):
    #     rc = RandomizedCollection()
    #     self.assertTrue(rc.insert(1))
    #     self.assertTrue(rc.remove(1))
    #     self.assertTrue(rc.insert(1))
    def test_2(self):
        rc = RandomizedCollection()
        self.assertTrue(rc.insert(1))
        self.assertFalse(rc.insert(1))
        self.assertTrue(rc.insert(2))
        self.assertFalse(rc.insert(2))
        self.assertFalse(rc.insert(2))
        self.assertTrue(rc.remove(1))
        self.assertTrue(rc.remove(1))
        self.assertTrue(rc.remove(2))
        self.assertTrue(rc.insert(1))
        self.assertTrue(rc.remove(2))
        
unittest.main()

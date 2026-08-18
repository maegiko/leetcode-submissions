# Last updated: 18/08/2026, 14:56:18
import random

class RandomizedSet:

    def __init__(self):
        self.setList = []
        self.elements = {}

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        else:
            self.setList.append(val)
            self.elements[val] = True
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.elements:
            self.setList.remove(val)
            self.elements.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.setList) - 1)
        return self.setList[idx]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
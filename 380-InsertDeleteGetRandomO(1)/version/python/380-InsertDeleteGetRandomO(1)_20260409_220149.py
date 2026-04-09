# Last updated: 09/04/2026, 22:01:49
1import random
2
3class RandomizedSet:
4
5    def __init__(self):
6        self.setList = []
7        self.elements = {}
8
9    def insert(self, val: int) -> bool:
10        if val in self.elements:
11            return False
12        else:
13            self.setList.append(val)
14            self.elements[val] = True
15            return True
16        
17
18    def remove(self, val: int) -> bool:
19        if val in self.elements:
20            self.setList.remove(val)
21            self.elements.pop(val)
22            return True
23        else:
24            return False
25        
26
27    def getRandom(self) -> int:
28        idx = random.randint(0, len(self.setList) - 1)
29        return self.setList[idx]
30
31        
32
33
34# Your RandomizedSet object will be instantiated and called as such:
35# obj = RandomizedSet()
36# param_1 = obj.insert(val)
37# param_2 = obj.remove(val)
38# param_3 = obj.getRandom()
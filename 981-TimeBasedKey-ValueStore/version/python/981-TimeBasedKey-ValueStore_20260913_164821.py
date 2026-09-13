# Last updated: 13/09/2026, 16:48:21
1class TimeMap:
2
3    def __init__(self):
4        self.hashMap = defaultdict(list)
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        hashMap = self.hashMap
8        hashMap[key].append([timestamp, value])
9
10    def get(self, key: str, timestamp: int) -> str:
11        hashMap = self.hashMap
12
13        l, r = 0, len(hashMap[key]) - 1
14
15        while l <= r:
16            mid = (l + r) // 2
17
18            t = hashMap[key][mid][0]
19
20            if timestamp > t:
21                l = mid + 1
22            elif timestamp < t:
23                r = mid - 1
24            else:
25                return hashMap[key][mid][1]
26        
27        return hashMap[key][r][1] if r >= 0 else ""
28        
29
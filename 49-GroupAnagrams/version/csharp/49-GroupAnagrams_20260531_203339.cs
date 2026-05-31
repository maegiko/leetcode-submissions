// Last updated: 31/05/2026, 20:33:39
1public class Solution {
2    public IList<IList<string>> GroupAnagrams(string[] strs) {
3        Dictionary<string, List<string>> dic = new();
4
5        foreach(string s in strs) {
6            int[] count = new int[26];
7
8            char[] chars = s.ToCharArray();
9
10            foreach(char c in chars) {
11                count[c - 'a']++;
12            }
13            
14            string key = string.Join('#', count);
15            List<string> list = dic.GetValueOrDefault(key, new List<string>());
16            list.Add(s);
17            dic[key] = list;
18        }
19
20        return dic.Values.Select(l => (IList<string>)l).ToList();
21    
22    }
23}
// Last updated: 18/08/2026, 14:58:12
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> dic = new();

        foreach(string s in strs) {
            int[] count = new int[26];

            char[] chars = s.ToCharArray();

            foreach(char c in chars) {
                count[c - 'a']++;
            }
            
            string key = string.Join('#', count);
            List<string> list = dic.GetValueOrDefault(key, new List<string>());
            list.Add(s);
            dic[key] = list;
        }

        return dic.Values.Select(l => (IList<string>)l).ToList();
    
    }
}
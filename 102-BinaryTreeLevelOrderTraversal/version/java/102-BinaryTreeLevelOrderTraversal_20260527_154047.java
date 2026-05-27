// Last updated: 27/05/2026, 15:40:47
1/**
2 * Definition for a binary tree node.
3 * public class TreeNode {
4 *     int val;
5 *     TreeNode left;
6 *     TreeNode right;
7 *     TreeNode() {}
8 *     TreeNode(int val) { this.val = val; }
9 *     TreeNode(int val, TreeNode left, TreeNode right) {
10 *         this.val = val;
11 *         this.left = left;
12 *         this.right = right;
13 *     }
14 * }
15 */
16class Solution {
17    public List<List<Integer>> levelOrder(TreeNode root) {
18        Deque<TreeNode> queue = new ArrayDeque<>();
19        List<List<Integer>> res = new ArrayList<>();
20
21        if (root == null) {
22            return res;
23        }
24
25        queue.offerLast(root);
26
27        while (!queue.isEmpty()) {
28            int levelSize = queue.size();
29            List<Integer> levels = new ArrayList<>();
30
31            for (int i = 0; i < levelSize; i++) {
32                TreeNode node = queue.pollFirst();
33                levels.add(node.val);
34
35                if (node.left != null)
36                    queue.offerLast(node.left);
37
38                if (node.right != null)
39                    queue.offerLast(node.right);
40            }
41
42            res.add(levels);
43        }
44
45        return res;
46    }
47}
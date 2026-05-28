// Last updated: 28/05/2026, 16:39:53
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
17    public List<Double> averageOfLevels(TreeNode root) {
18        Deque<TreeNode> queue = new ArrayDeque<>();
19        queue.offerLast(root);
20
21        List<Double> result = new ArrayList<>();
22
23        while (!queue.isEmpty()) {
24            int size = queue.size();
25            double levelTotal = 0;
26
27            for (int i = 0; i < size; i++) {
28                TreeNode node = queue.pollFirst();
29                int value = node.val;
30                levelTotal += value;
31
32                if (node.left != null) {
33                    queue.offerLast(node.left);
34                }
35
36                if (node.right != null) {
37                    queue.offerLast(node.right);
38                }
39            }
40
41            Double average = levelTotal / size;
42            result.add(average);
43        }
44
45        return result;
46    }
47}
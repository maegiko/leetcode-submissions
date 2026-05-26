// Last updated: 26/05/2026, 14:15:58
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
17    public TreeNode invertTree(TreeNode root) {
18        if (root == null)
19            return null;
20
21        if (root.left == null && root.right == null)
22            return root;
23        else {
24            TreeNode temp = root.left;
25            root.left = root.right;
26            root.right = temp;
27        }
28        
29        invertTree(root.left);
30        invertTree(root.right);
31
32        return root;
33    }
34}
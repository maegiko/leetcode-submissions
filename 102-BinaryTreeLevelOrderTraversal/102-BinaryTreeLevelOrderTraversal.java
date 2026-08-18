// Last updated: 18/08/2026, 14:57:40
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        List<List<Integer>> res = new ArrayList<>();

        if (root == null) {
            return res;
        }

        queue.offerLast(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> levels = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.pollFirst();
                levels.add(node.val);

                if (node.left != null)
                    queue.offerLast(node.left);

                if (node.right != null)
                    queue.offerLast(node.right);
            }

            res.add(levels);
        }

        return res;
    }
}
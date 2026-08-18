// Last updated: 18/08/2026, 14:56:05
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
    public List<Double> averageOfLevels(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.offerLast(root);

        List<Double> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            int size = queue.size();
            double levelTotal = 0;

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.pollFirst();
                int value = node.val;
                levelTotal += value;

                if (node.left != null) {
                    queue.offerLast(node.left);
                }

                if (node.right != null) {
                    queue.offerLast(node.right);
                }
            }

            Double average = levelTotal / size;
            result.add(average);
        }

        return result;
    }
}
// Last updated: 08/04/2026, 12:40:00
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int doMaxDepth(struct TreeNode* node, int *max) {
    if (node == NULL) return 0;

    int heightL = doMaxDepth(node->left, max);
    int heightR = doMaxDepth(node->right, max);

    if (heightL > heightR) {
        if (heightL > *max) *max = heightL;
        return heightL + 1;
    } else {
        if (heightR > *max) *max = heightR;
        return heightR + 1;
    }
}

int maxDepth(struct TreeNode* root) {
    if (root == NULL) return 0;
    int max = 0;
    doMaxDepth(root, &max);
    return max + 1;
}
class Solution {
public:
    int sum = 0;

    TreeNode* bstToGst(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        bstToGst(root->right);
        sum += root->val;
        root->val = sum;
        bstToGst(root->left);

        return root;
    }
};
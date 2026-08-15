class Solution {
public:
    TreeNode* prev = NULL;
    TreeNode* first = NULL;
    TreeNode* sec = NULL;

    void inorder(TreeNode* root) {
        if (root == NULL) return;
        inorder(root->left);

        if (prev != NULL && prev->val > root->val) {
            if (first == NULL) {
                first = prev;
            }
            sec = root;
        }
        prev = root;
        inorder(root->right);
    }

    void recoverTree(TreeNode* root) {
        inorder(root);
        int temp = first->val;
        first->val = sec->val;
        sec->val = temp;
    }
};

// Time Complexity   : O(n)
// Space Complexity  : O(h)
// by ar-sayeem [August 15, 2026]
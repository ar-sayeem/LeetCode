class Solution {
public:
    TreeNode* nextRight = NULL;

    void flatten(TreeNode* root) {
        if (root == NULL) {
            return;
        }

        flatten(root->right);
        flatten(root->left);

        root->left = NULL;
        root->right = nextRight;

        nextRight = root;
    }
};

// Time Complexity: O(N)
// Space Complexity: O(H)
// by ar-sayeem [July 17, 2026]
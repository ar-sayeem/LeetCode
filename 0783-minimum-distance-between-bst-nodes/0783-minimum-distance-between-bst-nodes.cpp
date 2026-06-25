class Solution {
public:
    TreeNode* prev = NULL;
    int minDiffInBST(TreeNode* root) {
        if (root == NULL) {
            return INT_MAX;
        }
        int ans = INT_MAX;
        if (root->left != NULL) {
            int leftMin = minDiffInBST(root->left);
            ans = min(ans, leftMin);
        }
        if (prev != NULL) {
            ans = min(ans, root->val - prev->val);
        }
        prev = root;
        if (root->right != NULL) {
            int rightMin = minDiffInBST(root->right);
            ans = min(ans, rightMin);
        }
        return ans;
    }
};

// Time Complexity   : O(N)
// Space Complexity  : O(1)
// by ar-sayeem [June 19, 2026]
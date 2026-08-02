class Solution {
public:
    int preOrder = 0;

    int kthSmallest(TreeNode* root, int k) {
        if (root == NULL) {
            return -1;
        }
        if (root->left != NULL) {
            int leftAns = kthSmallest(root->left, k);
            if (leftAns != -1) {
                return leftAns;
            }
        }

        if (preOrder + 1 == k) {
            return root->val;
        }

        preOrder = preOrder + 1;

        if (root->right != NULL) {
            int rightAns = kthSmallest(root->right, k);
            if (rightAns != -1) {
                return rightAns;
            }
        }

        return -1;
    }
};

// Time Complexity: O(H + K)
// Space Complexity: O(H)
// by ar-sayeem [August 02, 2026]
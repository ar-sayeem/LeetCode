class Solution {
public:
    int search(vector<int>& inorder, int left, int right, int val) {
        for (int i = left; i <= right; i++) {
            if (inorder[i] == val) {
                return i;
            }
        }

        return -1;
    }

    TreeNode* helper(vector<int>& postorder, vector<int>& inorder, int& postIdx,
                     int left, int right) {
        if (left > right) {
            return NULL;
        }

        TreeNode* root = new TreeNode(postorder[postIdx]);

        int inIdx = search(inorder, left, right, postorder[postIdx]);
        postIdx--;

        root->right = helper(postorder, inorder, postIdx, inIdx + 1, right);
        root->left = helper(postorder, inorder, postIdx, left, inIdx - 1);

        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int postIdx = postorder.size() - 1;

        return helper(postorder, inorder, postIdx, 0, inorder.size() - 1);
    }
};

// Time Complexity: O(n²)
// Space Complexity: O(h)
// by ar-sayeem [July 22, 2026]
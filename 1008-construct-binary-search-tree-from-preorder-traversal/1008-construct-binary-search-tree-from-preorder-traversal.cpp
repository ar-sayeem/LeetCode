class Solution {
public:
    TreeNode* helper(vector<int>& preorder, int &i, int bound){
        if(i >= preorder.size() || preorder[i] > bound){
            return NULL;
        }

        TreeNode* root = new TreeNode(preorder[i++]);
        root->left = helper(preorder, i, root->val);
        root->right = helper(preorder, i, bound);

        return root;
    }

    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int i = 0;
        return helper(preorder, i, INT_MAX);
    }
};

// Time Complexity   : O(N)
// Space Complexity  : O(N)
// by ar-sayeem [August 17, 2026]
class BSTIterator {
public:
    stack<TreeNode*> s;

    void storeLeftNodes(TreeNode* root) {
        while (root != NULL) {
            s.push(root);
            root = root->left;
        }
    }

    BSTIterator(TreeNode* root) { storeLeftNodes(root); }

    int next() {
        TreeNode* ans = s.top();
        s.pop();

        storeLeftNodes(ans->right);
        return ans->val;
    }

    bool hasNext() { return s.size() > 0; }
};

// Time Complexity   : O(1)
// Space Complexity  : O(h)
// by ar-sayeem [August 29, 2026]
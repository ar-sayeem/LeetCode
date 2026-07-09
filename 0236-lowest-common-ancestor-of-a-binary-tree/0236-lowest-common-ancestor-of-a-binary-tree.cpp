class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL){
            return NULL;
        }

        if (root->val == p->val || root->val == q->val){
            return root;
        }

        TreeNode* leftLCA = lowestCommonAncestor(root->left, p, q);
        TreeNode* rightLCA = lowestCommonAncestor(root->right, p, q);

        if(leftLCA && rightLCA){
            return root;
        }
        else if(leftLCA != NULL){
            return leftLCA;
        }
        else{
            return rightLCA;
        }
    }
};

// Time Complexity: O(N)
// Space Complexity: O(N)
/// by ar-sayeem [July 09, 2026]
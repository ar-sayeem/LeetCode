class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL){
            return NULL;
        }

        if(root->val > p->val && root->val > q->val){
            return lowestCommonAncestor(root->left, p, q);
        }
        else if(root->val < p->val && root->val < q->val){
            return lowestCommonAncestor(root->right, p, q);
        }
        else{
            return root;
        }
    }
};

// Time Complexity   : O(H)
// Space Complexity  : O(H)
// by ar-sayeem [June 19, 2026]
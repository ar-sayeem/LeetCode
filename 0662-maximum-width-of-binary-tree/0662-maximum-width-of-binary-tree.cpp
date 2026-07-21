class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        queue<pair<TreeNode*, unsigned long long int>> q;
        q.push({root, 0});
        int maxWidth = 0;

        while (q.size() > 0) {
            int currLevelSize = q.size();
            unsigned long long int stIdx = q.front().second;
            unsigned long long int endIdx = q.back().second;

            maxWidth = max(maxWidth, (int)(endIdx - stIdx + 1));

            for (int i = 0; i < currLevelSize; i++) {
                auto curr = q.front();
                q.pop();
                if (curr.first->left) {
                    q.push({curr.first->left, curr.second * 2 + 1});
                }
                if (curr.first->right) {
                    q.push({curr.first->right, curr.second * 2 + 2});
                }
            }
        }
        return maxWidth;
    }
};

// Time Complexity   : O(N)
// Space Complexity  : O(N)
// by ar-sayeem [July 21, 2026]
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int n = nums.size();

        if (n < 3)
            return ans;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 2; i++) {

            // Early stopping optimization
            if (nums[i] > 0)
                break;

            // Skip duplicate i values
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                long sum = (long)nums[i] + nums[left] + nums[right];

                if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                } else {
                    ans.push_back({nums[i], nums[left], nums[right]});

                    left++;
                    right--;

                    // Skip duplicate left values
                    while (left < right && nums[left] == nums[left - 1])
                        left++;

                    // Skip duplicate right values
                    while (left < right && nums[right] == nums[right + 1])
                        right--;
                }
            }
        }
        return ans;
    }
};

// Time Complexity : O(n ^ 2)
// Space Complexity : O(1) // excluding output
// by ar-sayeem [February 13, 2026]
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        int n = nums.size();
        sort(nums.begin(), nums.end());

        // stop at n-3 to have room for j, p, q
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue; // skip duplicates for i

            // stop at n-2 to have room for p, q
            for (int j = i + 1; j < n - 2;) {

                int p = j + 1, q = n - 1;
                while (p < q) {
                    long long sum = (long long)nums[i] + (long long)nums[j] +
                                    (long long)nums[p] + (long long)nums[q];

                    if (sum < target) {
                        p++;
                    } else if (sum > target) {
                        q--;
                    } else { // sum == target
                        ans.push_back({nums[i], nums[j], nums[p], nums[q]});
                        p++;
                        q--;

                        while (p < q && nums[p] == nums[p - 1])
                            p++; // skip duplicates for p
                        // no need optimization for q
                        while (p < q && nums[q] == nums[q + 1])
                            q--;
                    }
                }

                j++;
                while (j < n - 2 && nums[j] == nums[j - 1])
                    j++; // skip duplicates for j
            }
        }
        return ans;
    }
};

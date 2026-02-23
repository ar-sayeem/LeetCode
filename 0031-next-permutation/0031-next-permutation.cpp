class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int pivot = -1;
        for (int i = n-2; i >= 0; i--){
            if(nums[i] < nums[i+1]){
                pivot = i;
                break;
            }
        }
        if(pivot == -1){
            reverse(nums.begin(), nums.end());     // in place changes
            return;
        }
        // next larger element
        for(int i = n-1; i > pivot; i--){
            if(nums[i] > nums[pivot]){
                swap(nums[i], nums[pivot]);
                break;
            }
        }

        // reverse (pivot+1 to n-2)
        int i = pivot+1;
        int j = n - 1;
        while(i <= j){
            swap(nums[i++], nums[j--]);     // revere(nums.begin() + pivot + 1, nums.end())
        }

    }
};


# Time Complexity: O(n)
# Space Complexity: O(1)
# by ar-sayeem [February 23, 2026]
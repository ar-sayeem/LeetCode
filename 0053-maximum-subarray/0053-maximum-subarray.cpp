class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Kadane's Algorithm
        int CS = 0, MS = INT_MIN;
        for(int i : nums)
        {
            CS += i;
            MS = max(CS, MS);
            if(CS < 0)
            {
                CS = 0;
            }
        }

        return MS;
    }
};

// CS = CurrentSum | MS = MaxSum
// Time Complexity : O(n)
// Space Complexity : O(1)
// by ar - sayeem[Month Date, 2026]
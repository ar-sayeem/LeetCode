class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;

        for (int price : prices) {
            if (price < min_price) {
                min_price = price;
            } else {
                int profit = price - min_price;
                if (profit > max_profit) {
                    max_profit = profit;
                }
            }
        }

        return max_profit;
    }
};

// Time Complexity: O(n)
// Space Complexity: O(1)
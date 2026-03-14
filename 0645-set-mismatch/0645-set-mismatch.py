class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        exp_sum = n * (n + 1) // 2
        exp_sum_sq = n * (n + 1) * (2 * n + 1) // 6

        act_sum = sum(nums)
        act_sum_sq = sum(x * x for x in nums)                       # squeare sum of each number

        dup_minus_mis = act_sum - exp_sum                           # actual - expected
        dup_plus_mis = (act_sum_sq - exp_sum_sq) // dup_minus_mis   # ( actual - expected ) // dup_minus_mis

        dup = (dup_minus_mis + dup_plus_mis) // 2
        mis = dup_plus_mis - dup

        return [dup, mis]


# Time Complexity: O(N)
# Space Complexity: O(1)
# by ar-sayeem [March 14,2026]
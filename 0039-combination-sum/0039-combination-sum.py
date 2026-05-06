from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        nums = candidates
        n = len(nums)
        
        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            if cur_sum > target or i == n:
                return
            
            # skip current number
            backtrack(i + 1, cur_sum)
            
            # take current number
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            sol.pop()
        
        backtrack(0, 0)
        return res

# Time Complexity   : O(2^(target/min(candidates)))
# Space Complexity  : O(target/min(candidates))
# by ar-sayeem [May 06, 2026]